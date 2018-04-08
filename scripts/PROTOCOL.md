# Script protocol

This is the documentantion for the interface/protocol which should be able to handle both python and shell scripts. However there is nothing stopping someone to write a script at another language. As long as it can be executed by linux and it provides valid output it should work.

## How are scripts executed

The directory 'scripts' is searched recursively and in alphabetical order. Each time a new directory is 'read', a new subcategory is created with the name of the directory. Any new registration will be stored inside that subcategory. The way this is displayed to the user can and will change. Else if the file is a [python](#python) script, it is imported and executed. Else the file is executed only if the executable bit is set and its output is parsed as defined in the [other](#other-executables) section.

### Python

Each python script should call registerEntry on any new entries it wants to register. registerEntry takes two arguments. The first one is a string which is also the key. The second argument is an object which extends BaseEntry. These scripts also inherit the global variables of the main program.

### Other executables

The output in stdout should contain any number of the following commands. Each command takes a number of arguments, which are split by any number of whitespace.

* **`KVAL`** _`key`_ _`value`_

&nbsp;&nbsp;Adds a basic key=value entry to the registry.
&nbsp;&nbsp;key: a string of characters. It can only contain alphanumeric and underscores.
&nbsp;&nbsp;value: a string such as `"I am a string"`
___
A list of special environment variables are also defined. But for now only GENUME_VERSION is defined.