#!/usr/bin/env python3

# Execute with
# $ python genume/__main__.py (2.6+)
# $ python -m genume          (2.7+)

import sys
import os.path
import logging

from genume.logging.logger import init as initLogger
from genume.genume import main

if __package__ is None and not hasattr(sys, 'frozen'):
    # direct call of __main__.py
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

if __name__ == '__main__':
    initLogger()
    main()
