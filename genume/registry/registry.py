from pathlib import Path
import logging as log
from threading import Thread, Lock, Condition
import re

from gi.repository import GObject

from genume.constants import SCRIPTS_ROOT, SCRIPTS_IGNORE
from genume.registry.category import CategoryEntry
from genume.registry.xparser import run_and_parse


def match_list(s, l):
    "Match any regex test."
    for i in l:
        if re.match(i, s):
            return True
    return False


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
        self.cond = Condition()
        self.root = None
        # Fire up the thread.
        self.start()

    def run(self):
        log.info("Registry helper thread is starting up...")
        while True:
            self.cond.acquire()
            if self.cond.wait():
                log.info("Registry is refreshing...")
                # Actual refresh goes here.
                log.info("Registry has finished refreshing.")
                self.cond.release()

    def request_refresh(self):
        "This method reloads the enumeration by running all the scripts(async version)."
        self.cond.acquire()
        self.cond.notify()
        self.cond.release()

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
