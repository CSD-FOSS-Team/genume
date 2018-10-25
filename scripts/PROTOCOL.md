# Script protocol

Genume traverses the files under `script/` in alphabetical order every time it needs to update the enumeration. For every file in every directory it finds it performs the next steps:

1. Ignores the file if it matches at least one regex from `SCRIPTS_IGNORE`.
2. If the file is a directory, then it creates a new category and performs the same steps for all the files of the new directory.
3. Finally if the **executable** bit is set, the file gets executed. One can then communicate with the host program as described in sections [bash](#bash) for generic shell scripts or at the [lower level protocol](#low-level) for everything that is not a script.

## Bash

- Communication with other executable formats happens with environment variables and pipes.

### Getting input

Input from genume happens mostly with environment variables.

1. `GENUME_VERSION`
    - A string representing the genume version that is running this script. If this variable is not set, then your executable is probable run outside of genume.

## Low Level

- Communication with other executable formats happens with environment variables and pipes.

### Getting input

Input from genume happens mostly with environment variables.

1. `GENUME_VERSION`
    - A string representing the genume version that is running this script. If this variable is not set, then your executable is probable run outside of genume.

### Creating entries

Entries are created by parsing the output of the script. As a result it must output any number of the below sequences to modify the enumeration.

```
[VALUE|VALUES] [BAS|ADV] key value
[GROUP|PATH] [BAS|ADV] path
[VALUE|VALUES] [BAS|ADV] key value [GROUP|PATH] path
```

1. `VALUE [BAS|ADV] key value`
    - Creates a new entry containing a simple string.
    - `VALUE` is the command name.
    - `[BAS|ADV]` is an enum. It is either `BAS` for **basic** or information or `ADV` for **advanced** information.
    - `key` is the key. It should contain only characters you would use to name a variable _(aka alphanumeric and underscores)_.
    - `value` is the string to display. It must be between double quotation marks.

2. `VALUES [BAS|ADV] key value`
    - Creates a new entry containing a list with the single string value passed. If the key already exists, it adds the value to the list.
    - `VALUES` is the command name.
    - `[BAS|ADV]` is an enum. It is either `BAS` for **basic** or information or `ADV` for **advanced** information.
    - `key` is the key. It should contain only characters you would use to name a variable _(aka alphanumeric and underscores)_.
    - `value` is one of the strings to display. It must be between double quotation marks.

3. `GROUP [BAS|ADV] name`
    - Defines a new group. All following commands will refer to the new group untill a new group or path command.

4. `PATH [BAS|ADV] path`
    - Equivalent to the group command except the given value correspnds to a path of groups. The groups in the path are separated with `.`

5. `[VALUE|VALUES] [BAS|ADV] key value [GROUP|PATH] path`
    - A combination of the value and group commands
    - The group or path specified for this command will not affect the folloing commands.

#### Notes

- The values will be trimmed of whitespace.

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
