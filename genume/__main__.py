#!/usr/bin/env python3

# Execute with:
# python -m genume

import sys
import os.path
import logging

from genume.logging.logger import init as initLogger
from genume.extract import extract
from genume.genume import main


def consoleentry():
    initLogger()
    extract()
    main()


if __package__ is None and not hasattr(sys, 'frozen'):
    # direct call of __main__.py
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))

if __name__ == '__main__':
    consoleentry()
