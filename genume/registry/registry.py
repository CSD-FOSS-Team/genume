import re

from genume.globals import SCRIPTS_ROOT, SCRIPTS_IGNORE
from genume.registry.base import PythonScript
from genume.registry.category import CategoryEntry
from genume.registry.xparser import run_and_parse

def match_list(s, l):
    for i in l:
        if re.match(i, s):
            return True
    return False

class Registry:
    "Class which transparently provides access to the enumeration."
    # Constructor
    def __init__(self):
        # Initialize root.
        self.root = CategoryEntry()
    def update(self):
        "This method reloads the enumeration by running all the scripts."
        self.root = CategoryEntry()
        self._handle_dir(self.root, SCRIPTS_ROOT)
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
            elif file.suffix == ".py":
                # Python script case.
                PythonScript.runscript(cat, file)
            else:
                # Generic executable case.
                run_and_parse(cat, file)