# Script protocol

Genume traverses the files under `script/` in alphabetical order every time it needs to update the enumeration. For every file in every directory it finds it performs the next steps:

1. Ignores the file if it matches at least one regex from `SCRIPTS_IGNORE`.
2. If the file is a directory, then it creates a new category and performs the same steps for all the files of the new directory.
3. Finally if the **executable** bit is set, the file gets executed. One can then communicate with the host program as described in sections [bash](#bash) for generic shell scripts or at the [lower level protocol](#low-level) for everything that is not a script.

## Bash

- For bash scripts there are some helper executables. For more information read [bash helpers](../bash_helpers/README.md). For more advanced usage the [low level](#low-level) can also be used directly.

## Low Level

- Communication with the host program happens threw environment variables and pipes/streams.

### Input

Constants are passed from the host program to the child as environments variables. These currently are:

1. `HOST_VERSION`
    - A string representing the host version that is running this script. If this variable is not set, then your executable is probably getting run in a terminal.

2. `HOST_NAME`
    - A string containing the name of the host program.

3. `HOST_DESC`
    - A string containing a small description of the host program.

4. `MASTER_CATEGORY`
    - Contains the name of the root category of the current child. Any new entries will go under this category.

### Communicating with the host

Commands are sent to the host by writing to stdout. Responses, if specified by the command are sent to the stdin of the child process. Stderr gets redirected to host's stdout.

```sh
CONF id [dependencies...]
SET DESCRIPTION value
VALUE [BAS|ADV] [SUBCAT path] key value...
SUBCAT [BAS|ADV] path
```

1. `CONF [dependencies...]`
    - Configures the child process. This must be sent only once and be the first command sent.
    - `dependencies` is a variable size set of strings of all the external executables the child needs. One custom dependency is `root`, which provides root access to the child(if allowed by the user).
    - This commands replies with `OK` if everything has been setup correctly. Else it replies with an error message.

2. `SET DESCRIPTION value`
    - Changes a property to a new value.
    - Currently supported properties are:
        1. `DESCRIPTION`: The description of the current (sub)category (string).

3. `VALUE [BAS|ADV] [SUBCAT path] key value...`
    - Creates a new entry containing a string or multiples.
    - `VALUE` is the command name.
    - `[BAS|ADV]` is an optional enum. It is either `BAS` for **basic** or information or `ADV` for **advanced** information. It has no effect if the entry already exists.
    - `[SUBCAT path]` is an optional subcategory. Unlike the full command the effects of this option are temporary.
    - `key` is the key. It should contain only characters you would use to name a variable _(aka alphanumeric and underscores)_.
    - `value...` is the string or strings to display. Each one must be between double or single quotation marks or parenthesis.

4. `SUBCAT [BAS|ADV] path`
    - Creates a new subcategory or switches to an already existing one. All following commands will refer to the new subcategory until a new subcat command.
    - `SUBCAT` the command name.
    - `[BAS|ADV]` is an optional enum. It is either `BAS` for **basic** or information or `ADV` for **advanced** information. It has no effect if the category already exists.
    - `path` is the path of the subcategory to switch to. Two subcategories must be seperated by a dot and should only contain alphanumeric and underscores. Paths starting with dot (.) are interpreted as relative paths. An empty path is interpreted as the master/root category.

#### Notes

- String values will be trimmed of leading and trailing whitespace.
