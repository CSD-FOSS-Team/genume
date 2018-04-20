#!/usr/bin/env python3

# Execute with
# $ python genume/__main__.py (2.6+)
# $ python -m genume          (2.7+)

# TODO import Gtk only if the gui will be shown
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import sys
import os.path

if __package__ is None and not hasattr(sys, 'frozen'):
    # direct call of __main__.py
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

import genume.terminterface as cli
import genume.view.main as gui

if __name__ == '__main__':

    # cli.main()

    gui.main()
    Gtk.main()
