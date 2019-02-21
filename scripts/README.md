# Scripts

This where all the scripts go. For more info about the script interface and examples please go to [PROTOCOL.md](PROTOCOL.md).

## Styleguide

The scripts ought to abide to [Google's Shell Styleguide](https://google.github.io/styleguide/shell.xml).
**Important**: Note that 4 spaces are used for indentation instead of the above link's suggested 2.

## Files/directories of interest

1. `/proc` and `/sys`
    - These folders are managed by the kernel and the loaded drivers(modules in linux terms). For more information you can read the official documentation in one of the following links.
        - [Linux Filesystem Hierarchy](http://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html)
        - [Linux ABI documentation](https://github.com/torvalds/linux/tree/master/Documentation/ABI)
        - [Linux proc documentation](https://github.com/torvalds/linux/blob/master/Documentation/filesystems/proc.txt)
2. `/etc` and `/home`
    - These directories store program configurations files. As a result there is no insurance that they will continue to exist or that there will be no changes to their structure. So please be carefull when reading files from these directories.