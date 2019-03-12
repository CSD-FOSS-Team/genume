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

## New to Genume

If you are new to Genume and would like to learn more, we recommend reviewing the [getting started] documentation.

[getting started]: docs/learning-genume

## Get Genume

You can download Genume's source code by

```sh
git clone https://github.com/CSD-FOSS-Team/genume.git
```

See [working with the Genume repository](docs/git) for more information.

Build with Python 3 and Gtk+3.

Start Genume by running `make` or `python3 -m genume`.

## Developing and Contributing

Please see the [Contribution Guide][] for how to develop and contribute.

[Contribution Guide]: .github/CONTRIBUTING.md

## Support

For support please see the [Support Section][].

[Support Section]: .github/SUPPORT.md

## Legal and Licensing

All files in this repository are Copyright (c) 2018 **genume author list**_(Usually available in AUTHORS)_.

Code and documentation in this repository is licensed under the [GNU General Public License v2.0][], unless explicitly stated otherwise.

Data in this repository is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/), unless explicitly stated otherwise.

An up to date **genume author list** can be determined via `git shortlog -sne`.

[GNU General Public License v2.0]: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html

## Features

Genume utilizes a custom [protocol][] and [bash helpers][], which reinforces the core design idea of heavy modularity. By default genume displays the collected information in a GUI, but it can also export the enumeration in a wide range of various file formats. Visit the [getting started] documentation.

[getting started]: docs/learning-genume

## Build and Install