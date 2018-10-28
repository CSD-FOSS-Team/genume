from pathlib import Path
import logging as log
from threading import Thread, Semaphore
import re
from enum import Enum
import os
from collections import deque

from gi.repository import GObject

from genume.constants import SCRIPTS_ROOT, SCRIPTS_IGNORE, MAX_MULTIEXE
from genume.registry.category import CategoryEntry
from genume.registry.child import ChildHandler


def match_list(s, l):
    "Match any regex test."
    for i in l:
        if re.match(i, s):
            return True
    return False


RegistryStates = Enum("RegistryStates", "waiting start scanning collecting finish")


class Registry(Thread, GObject.Object):
    """Class which transparently provides access to the enumeration."""
    _instance_count = 0

    def __init__(self, scripts_path=Path(SCRIPTS_ROOT)):
        # Required by the thread class.
        super().__init__(name="Registry-%i" % (Registry._instance_count), daemon=True)
        Registry._instance_count += 1
        # Prepare fields.
        if isinstance(scripts_path, str):
            scripts_path = Path(scripts_path)
        elif not isinstance(scripts_path, Path):
            raise ValueError("scripts_path must be either a string or a Path.")
        self.path = scripts_path
        self.lock = Semaphore()
        self.state = RegistryStates.waiting
        self.root = None
        # Fire up the thread.
        self.start()

    def scan_ahead(self):
        child_list = []
        self.root = CategoryEntry(path=self.path)
        pending_cats = deque([self.root])
        while len(pending_cats) != 0:
            current_cat = pending_cats.pop()
            current_path = current_cat.path
            log.info("Currently scanning: %s" % (current_path.name))
            for file in sorted(current_path.iterdir()):
                if match_list(file.name, SCRIPTS_IGNORE):
                    # Ignore case.
                    log.warning("Ignoring: %s" % (file.name))
                elif file.is_dir():
                    # Directory case.
                    new_cat = CategoryEntry(parent=current_cat, path=file)
                    key = file.name
                    current_cat[key] = new_cat
                    log.debug("Adding new category: %s" % (key))
                    pending_cats.appendleft(new_cat)
                else:
                    # Executable case.
                    if os.access(str(file), os.X_OK):
                        new_child = ChildHandler(path=file, root_cat=current_cat)
                        log.debug("Adding new executable: %s" % (file.name))
                        child_list.append(new_child)
                    else:
                        log.warning("Ignoring: %s" % (file.name))
        return child_list

    def execute_children(self, pending_children):
        executing = [None] * MAX_MULTIEXE
        # TODO: similar to how modern cpus handle parallel execution in the same core(pending_children are the instructions and executing[] are the 'parallel' units).

    def run(self):
        log.info("Registry helper thread is starting up...")
        while True:
            if self.lock.acquire(blocking=True) and self.state is RegistryStates.start:
                log.info("Registry is refreshing...")
                # Actual refresh starts here.
                # First scan the directories.
                self.state = RegistryStates.scanning
                pending_children = self.scan_ahead()
                # Take a break to process events.
                # TODO: GLib.idle_add
                # Start collecting and parsing commands in steps so the main threads can continue processing.
                self.state = RegistryStates.collecting
                self.execute_children(pending_children)
                # Change state and prepare to hand data to main thread.
                self.state = RegistryStates.finish
                log.info("Registry has finished refreshing.")

    def request_refresh(self):
        "This method reloads the enumeration by running all the scripts(async version)."
        if self.state is RegistryStates.waiting:
            self.state = RegistryStates.start
            self.lock.release()
            return True
        else:
            raise RuntimeError("Refresh requested but registry is in an invalid state!")

    def get_async_data(self):
        "Gets data(an Entry tree) after a refresh request has finished. Else returns false."
        if self.state is RegistryStates.finish:
            # Reset state to prepare for next refresh.
            self.state = RegistryStates.waiting
            return self.root
        else:
            return False

    def refresh(self):
        "This method reloads the enumeration by running all the scripts(synchronized version)."
        pass

    @staticmethod
    def _handle_dir(cat, path):
        "Internal static recursive method to find scripts."
        for file in sorted(path.iterdir()):
            if match_list(file.name, SCRIPTS_IGNORE):
                # Ignore case.
                pass
            elif file.is_dir():
                # Directory case.
                new_cat = CategoryEntry(cat)
                key = file.name
                cat[key] = new_cat
                Registry._handle_dir(new_cat, file)
            else:
                # Generic executable case.
                run_and_parse(cat, file)
