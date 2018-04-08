import weakref
from pathlib import Path

from category import Category

# Must be moved elsewhere.
SCRIPTS_ROOT_PATH = Path("scripts/")

# Internal helper functions
def _handle_python():
    pass

def _handle_other():
    pass

def _handle_dir(category, directory):
    print("Debug: handling directory {0} in category \"{1}\"".format(directory, category))
    # TODO: Alphabetical order.
    for c in directory.iterdir():
        if c.is_dir():
            # Create a new subcategory and run recursively for that category.
            subcat = Category(category)
            category[c.name] = subcat
            print("Debug: new subcategory {0}".format(c.name))
            _handle_dir(subcat, c)
        elif c.is_file():
            if c.suffix:
                pass
            else:
                pass

class Registry:
    # Is this really needed?
    instance = None
    # Constructor
    def __init__(self):
        if Registry.instance is not None and Registry.instance() is not None:
            raise RuntimeError("Only one registry instance should be created for now.")
        else:
            Registry.instance = weakref.ref(self)
            # Create root.
            self.root = Category()
    # This method updates/reload/refreshes the enumeration by running all the scripts.
    def update(self):
        _handle_dir(self.root, SCRIPTS_ROOT_PATH)
