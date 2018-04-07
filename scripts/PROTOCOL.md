# Script protocol

This is the documentantion for the interface/protocol which should be able to handle both python and shell scripts. However there is nothing stopping someone to write a script at another language. As long as it can be executed by linux and it provides valid output it should work.

## How are scripts executed

The directory 'scripts' is searched recursively. Each time a new directory is 'read', a new subcategory is created with the name of the directory. Any new registration will be stored inside that subcategory. The way this is displayed to the user can and will change. Else if the file is a [python](#Python) script, it is imported and executed. Else the file is executed only if the executable bit is set and its output is parsed as defined in the [other](#Other_executables) section.

### Python

//TODO

### Other executables

//TODO