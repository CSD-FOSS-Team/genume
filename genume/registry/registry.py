from pathlib import Path
import logging as log
from threading import Thread, Semaphore
from enum import Enum
import os
from collections import deque

from gi.repository import GObject

from genume.constants import SCRIPTS_ROOT, SCRIPTS_IGNORE
from genume.utils import match_list, make_signal_emitter, get_scripts_multidispatch_limit
from genume.registry.category import CategoryEntry
from genume.registry.child import ChildHandler


RegistryStates = Enum("RegistryStates", "waiting start scanning collecting finish")


class RegistryObserver(GObject.Object):
    """Private type to provide signal support for registry."""
    @GObject.Signal
    def scan_complete(self):
        pass

    @GObject.Signal
    def refresh_complete(self):
        pass


class Registry(Thread):
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
        self.observer = RegistryObserver()
        # Fire up the thread.
        self.start()

    def _scan_ahead(self):
        "Scans and parses directory structure."
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
                    log.debug("Ignoring: %s" % (file.name))
                elif file.is_dir():
                    # Directory case.
                    new_cat = CategoryEntry(parent=current_cat, path=file)
                    key = file.name
                    current_cat[key] = new_cat
                    pending_cats.appendleft(new_cat)
                else:
                    # Executable case.
                    if os.access(str(file), os.X_OK):
                        new_child = ChildHandler(path=file, root_cat=current_cat, parent=self)
                        child_list.append(new_child)
                    else:
                        log.warning("Ignoring: %s" % (file.name))
        return child_list

    def _execute_children(self, children):
        "Multi-dispatch children."
        # Children waiting execution.
        pending = deque(children)
        # Children currently under execution.
        executing = [None] * get_scripts_multidispatch_limit()
        while len(pending) != 0 or executing.count(None) != len(executing):
            for i, slot in enumerate(executing):
                if slot is None and len(pending) != 0:
                    # Get the next available child.
                    executing[i] = pending.popleft().start()
                elif slot is not None and slot.do_step():
                    # Child has finished, pick next one.
                    if len(pending) != 0:
                        executing[i] = pending.popleft().start()
                    else:
                        executing[i] = None
        # Finish up.
        for c in children:
            c.finish_up()

    def run(self):
        log.info("Registry thread is starting up...")
        while True:
            if self.lock.acquire(blocking=True) and self.state is RegistryStates.start:
                log.debug("A refresh has been requested.")
                # Actual refresh starts here.
                # First scan the directories.
                self.state = RegistryStates.scanning
                pending_children = self._scan_ahead()
                # Take a break to process events.
                GObject.idle_add(make_signal_emitter(self.observer, "scan_complete"))
                # Start collecting and parsing commands in steps,
                # so the main thread is not getting blocked.
                self.state = RegistryStates.collecting
                self._execute_children(pending_children)
                # Change state and prepare to hand data to main thread.
                self.state = RegistryStates.finish
                # Inform main thread.
                GObject.idle_add(make_signal_emitter(self.observer, "refresh_complete"))
                log.debug("Registry refresh has been completed.")

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
        "This method reloads the enumeration by running all the scripts(synchronized version). No glib main loop must be running!"
        # Registry needs a glib main loop to be running.
        self.observer.loop = GObject.MainLoop()
        # Register event handlers.
        self.observer.connect("refresh_complete", lambda self: self.loop.quit())
        # Start refresh.
        self.request_refresh()
        # Enter main loop.
        self.observer.loop.run()
        # Cleanup.
        del self.observer.loop
        # The refresh has already finished, so this resets the state and also returns the root.
        return self.get_async_data()
