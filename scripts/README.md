# Scripts

This where all the scripts go. For more info about the script interface and examples please go to [PROTOCOL.md](PROTOCOL.md).

## Styleguide

The scripts ought to abide to [Google's Shell Styleguide](https://google.github.io/styleguide/shell.xml).

**Important**: Note that 4 spaces are used for indentation
instead of the above link's suggested 2.

*Easy Mode*: You could use the script in whichever way you see fit
and then use a utility like [shfmt](https://github.com/mvdan/sh#shfmt) 
to automatically format it. Just open a terminal and fire the 
command `shfmt -i 4 -ci -w <script.sh>`

## Best Practices

* Avoid hard-coding anything unless it's absolutely necessary.

* Avoid a method that is too long and complex.
  In such case, separate it to multiple methods or even a nested class as you see fit.

* Stick to the DRY principle -- Don't Repeat Yourself.
    * Wrap the commonly used code in methods,
      or even put it in a utility class if that makes sense,
      so that the same code can be reused.
    * Check if the code for the same purpose already exists in the code base before inventing your own wheel.
      If you're having trouble understanding a piece of code somebody else wrote, ask around!
    
## Coding Conventions

As a general rule, our coding convention is to follow the style mentioned above.
However, if a file happens to differ in style from conventions defined here,
the existing style in that file takes precedence,
until a *maintainer* reformatts it.

Thus, when making changes, you may find some existing code goes against the conventions defined here.
In such cases, please avoid reformatting any existing code when submitting a PR as it obscures the functional changes of the PR.
A separate PR should be submitted for style-only changes, or you could ask a *maintainer* to dig in.

## Commenting Conventions

* Place the comment on a separate line, not at the end of a line of code.

* Begin comment text with an uppercase letter and end it with a period.

* Comments should be shebang-only (no multi line comment syntax shenaningans)

* Update existing comments when you are changing the corresponding code.

## Files/directories of interest

1. `/proc` and `/sys`
    - These folders are managed by the kernel and the loaded drivers(modules in linux terms). For more information you can read the official documentation in one of the following links.
        - [Linux Filesystem Hierarchy](http://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html)
        - [Linux ABI documentation](https://github.com/torvalds/linux/tree/master/Documentation/ABI)
        - [Linux proc documentation](https://github.com/torvalds/linux/blob/master/Documentation/filesystems/proc.txt)
2. `/etc` and `/home`
    - These directories store program configurations files. As a result there is no insurance that they will continue to exist or that there will be no changes to their structure. So please be carefull when reading files from these directories.