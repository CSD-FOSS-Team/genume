#!/usr/bin/env python3

import os, sys

from genume import terminterface

# Basic initialization script.
# Command-line parsing parsing etc.
# This file should not be imported.
def main():
    # Properly configure paths.
    install_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(install_path)
    if install_path not in sys.path:
        sys.path.append(install_path)
    # Run the requested gui.
    terminterface.run()

if __name__ == '__main__':
    main()
