import traceback as trc

from importlib import import_module as imp
from enum import Enum

# Base classes and other objects.

InfoLevel = Enum("InfoLevel", "basic advanced")

class BaseEntry:
    "Common base class for all registry entries."
    def __init__(self, parent=None, level=InfoLevel.basic):
        if parent is None or isinstance(parent, BaseEntry):
            self.parent = None
            self.level = level
        else:
            raise RuntimeError("Error: tried to create an entry with an invalid parent.")

class PythonScript:
    "Common base class for all python scripts."
    def __init__(self, category):
        if isinstance(category, BaseEntry):
            self.category = category
        else:
            raise RuntimeError("Python script was given an invalid category.")
    def register(self, key, entry):
        "Convenience function for registering a new entry."
        self.category[key] = entry
    def run(self):
        "Gets called every time there has been requested an update to the enumeration."
        NotImplementedError("Error: all python scripts must implement run().")
    @staticmethod
    def runscript(cat, file):
        name = file.name.replace(".py", "").upper()
        # Create module string.
        pkg = str(file).replace(".py", "").replace("/", ".")
        # Do import.
        try:
            mod = imp(pkg)
            scr = getattr(mod, name)(cat)
            scr.run()
        except Exception as e:
            print("Error: while running python script({0}:{1}):".format(pkg, name))
            print(e)
            trc.print_exc()