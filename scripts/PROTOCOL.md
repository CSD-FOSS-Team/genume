# Script protocol

Genume traverses the files under `script/` in alphabetical order every time it needs to update the enumeration. For every file in every directory it finds it performs the next steps:

1. Ignores the file if it matches at least one regex from `SCRIPTS_IGNORE`.
2. If the file is a directory, then it creates a new category and performs the same steps for all the files of the new directory.
3. If the file's extension equals `py`, then it is executed as a [python](#python) script.
4. Else if the executable bit is set, it is handled as a generic [executable](#other-executables).

## Python

Each python script must `from genume.registry.pyhandle import PythonScript` and create a subclass of `PythonScript` with class name the filename of the python script, excluding the extension, in all caps. It must also overwrite the `run` method and inside that method call the `register` method.

```py
from genume.registry.pyhandle import PythonScript
# Put this in a file named pyex.py
class PYEX(PythonScript):
    "Example python script."
    def run(self):
        # We just create a new entry with key "pytest" and value "Hello from python!!!"
        self.register("pytest", "Hello from python!!!")
```

## Other executables

- Communication with other executable formats happens with environment variables and pipes.

### Getting input

Input from genume happens mostly with environment variables.

1. `GENUME_VERSION`
    - A string representing the genume version that is running this script. If this variable is not set, then your executable is probable run outside of genume <sub><sup>\*<sub><sup>*hint*</sup></sub></sup></sub>.

### Creating entries

Entries are created by parsing the output of the script. As a result it must output any number of the below sequences to modify the enumeration.

1. `VALUE [BAS|ADV] key value`
    - Creates a new entry containing a simple string.
    - `VALUE` is the command name.
    - `[BAS|ADV]` is an enum. It is either `BAS` for **basic** or information or `ADV` for **advanced** information.
    - `key` is the key. It should contain only characters you would use to name a variable _(aka alphanumeric and underscores)_.
    - `value` is the string to display. It must be between double quotation marks.

1. `VALUES [BAS|ADV] key value`
    - Creates a new entry containing a list of strings.
    - `VALUES` is the command name.
    - `[BAS|ADV]` is an enum. It is either `BAS` for **basic** or information or `ADV` for **advanced** information.
    - `key` is the key. It should contain only characters you would use to name a variable _(aka alphanumeric and underscores)_.
    - `value` is one of the strings to display. It must be between double quotation marks.

### Example script

```sh
#!/bin/sh
# Don't forget to set the executable bit with chmod +x ./example.sh
if [ -z "$GENUME_VERSION" ]; then
    echo "Running outside of genume."
else
    echo "VALUE BAS test \"Hello from shell!!!\""
fi
```