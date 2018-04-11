from importlib import import_module as imp
import traceback as trc

from genume.registry.base import BaseEntry
from genume.registry.value import ValueEntry


class PythonScript:
    """Common base class for all python scripts."""

    def __init__(self, category):
        if isinstance(category, BaseEntry):
            self.category = category
        else:
            raise RuntimeError("Python script was given an invalid category.")

    def register(self, key, entry):
        """Convenience function for registering a new entry."""
        if isinstance(entry, str):
            entry = ValueEntry(self.category, entry)
        self.category[key] = entry

    def run(self):
        """Gets called every time there has been requested an update to the enumeration."""
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
