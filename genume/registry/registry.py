import weakref
import os, sys, inspect
import subprocess as sbpr
from subprocess import CalledProcessError
from pathlib import Path
from shlex import split as cmdsplit

from .category import Category
from .value import ValueEntry

# Must be moved elsewhere.
SCRIPTS_ROOT_PATH = Path("scripts/")

# Internal helper functions
def _handle_python(category, file):
    print("Handling python in {0} for {1}".format(category, file))
    # Do import.
    modp = ""
    for p in file.parts:
        repl = p.replace(".py", "")
        print(p, repl, modp)
        if(repl != p):
            # Final string with the name of the python script.
            modp = modp + repl
        else:
            modp = modp + repl + "."
    print("Debug: loading module: {0}".format(modp))
    m = __import__(modp, fromlist=["run"])
    print(sys.path)
    sys.path.append(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    print(sys.path)
    entries = {"Category": Category, "ValueEntry": ValueEntry}
    m.run(category, entries)
    del sys.path[-1]
    print(sys.path)

def _parse_other(cat, o):
    cmds = cmdsplit(o)
    curr = cmds.pop(0)
    while True:
        if curr == "KVAL":
            key = cmds.pop(0)
            value = cmds.pop(0)
            nkv = ValueEntry(cat, value)
            cat[key] = nkv
        else:
            print("Error: unknown command {0}".format(curr))
        # Get next command.
        if len(cmds) != 0:
            curr = cmds.pop(0)
        else:
            break



def _handle_other(category, file):
    print("Handling other in {0} for {1}".format(category, file))
    if os.access(file, os.X_OK):
        print("Executing {0}".format(file))
        # Execute
        os.putenv("GENUME_VERSION", "0.0.0")
        try:
            output = sbpr.check_output(str(file)).decode("utf-8").strip()
            print("Command {0} outputted \"{1}\"".format(file, output))
            _parse_other(category, output)
        except CalledProcessError as e:
            print("Command {0} failed with return code {1}".format(file, e.returncode))
    else:
        print("{0} is not executable.".format(file))

def _handle_dir(category, directory):
    print("Debug: handling directory {0} in category \"{1}\"".format(directory, category))
    for c in sorted(directory.iterdir()):
        if c.is_dir():
            # Create a new subcategory and run recursively for that category.
            subcat = Category(category)
            category[c.name] = subcat
            print("Debug: new subcategory {0}".format(c.name))
            _handle_dir(subcat, c)
        elif c.is_file():
            if c.suffix == ".py":
                _handle_python(category, c)
            else:
                _handle_other(category, c)

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
