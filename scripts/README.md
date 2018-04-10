# Scripts

This where all the scripts go. For more info about the script interface and examples please go to [PROTOCOL.md](PROTOCOL.md).

## Files/directories of interest

1. `/proc` and `/sys`
    - These folders are managed by the kernel and the loaded drivers(modules in linux terms). For more information you can read the official documentation in one of the following links.
        - [Linux Filesystem Hierarchy](http://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html)
        - [Linux ABI documentation](https://github.com/torvalds/linux/tree/master/Documentation/ABI)
        - [Linux proc documentation](https://github.com/torvalds/linux/blob/master/Documentation/filesystems/proc.txt)
2. `/etc` and `/home`
    - These directories store program configurations files. As a result there is no insurance that they exist or that there will be no changes to their structure. Please be carefull when reading from these directories.