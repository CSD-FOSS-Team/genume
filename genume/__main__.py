#!/usr/bin/env python3

# Execute with
# $ python genume/__main__.py (2.6+)
# $ python -m genume          (2.7+)

import sys

if __package__ is None and not hasattr(sys, 'frozen'):
    # direct call of __main__.py
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

# Please change the following lines when the gui is done.
import genume.terminterface as gui

if __name__ == '__main__':
    gui.main()
