# ![logo][] Genume - *Graphical ENUMEration*

**Genume** is a Linux graphical user interface utility tool that serves as a means
of providing the user with a plethora of enumeration scripts.

![build status][]
![python][]
![GPLv2][]
![Screenshot]

[logo]: assets/favicon.svg
[build status]: https://img.shields.io/travis/CSD-FOSS-Team/genume.svg
[python]: https://img.shields.io/badge/python-3.3,%203.4,%203.5,%203.6,%203.7-blue.svg
[GPLv2]: https://img.shields.io/badge/license-GPLv2-lightgrey.svg

[screenshot]: assets/screenshot_genume.png

## Features

Genume utilizes a custom [protocol][] and [bash helpers][], which reinforces the core design idea of heavy modularity. By default genume displays the collected information in a GUI, but it can also export the enumeration in a wide range of various file formats.

[protocol]: scripts/PROTOCOL.md
[bash helpers]: bash_helpers/README.md

## Get Genume

You can download Genume's source code by

```sh
git clone https://github.com/CSD-FOSS-Team/genume.git
```

Build with Python 3 and Gtk+3.

Start Genume by running `make` or `python3 -m genume`.

Please see the [Build and Install](#build-and-install) for more information.

## Developing and Contributing

Please see the [Contribution Guide][] for how to develop and contribute.

[Contribution Guide]: .github/CONTRIBUTING.md

**Important**: When authoring a pull request always do an **interactive rebase**, if you want to sync your fork with the master branch. For genume the `make update` target is available as a shortcut.

## Build and Install

First you must install gtk+3.0 python3-gi

### Ubuntu/Debian/Raspbian

Raspberry Pi is also supported!

```sh
sudo apt install gtk+3.0 python3-gi
```

### Fedora

```sh
sudo yum install python3-gobject gtk3
```

### Arch linux

```sh
sudo pacman -Sy python-gobject gtk3
```

Finally **inside the directory where you've download genume's source code** run:

```sh
python3 setup.py install
```

to install genume on your system.

## Legal and Licensing

All files in this repository are Copyright (c) 2018 **genume author list** _(Usually available in AUTHORS)_.

Code and documentation in this repository is licensed under the [GNU General Public License v2.0][], unless explicitly stated otherwise.

Data in this repository is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/), unless explicitly stated otherwise.

An up to date **genume author list** can be determined via `git shortlog -sne`.

[GNU General Public License v2.0]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html