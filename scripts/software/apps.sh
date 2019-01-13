#!/bin/bash

# check for an app and if it exists provide the version
function check() {
  name=$1
  version=$2

  key=$name

  if command -v "$name" >/dev/null; then
    echo VALUE BAS "$key" \"$($name $version 2>&1 | sed '/./q; d')\" GROUP "apps"
  fi
}

check "bash" "-version"
check "make" "--version"
check "git" "--version"

check "gnome-software" "--version"

'''
Programming Languages & Compilers
'''

# GNU Compiler Collection (C, C++, Go...)
check "gcc" "--version"
check "java" "-version"
check "python" "-V"
# Haskell Compiler
check "ghci" "--version"
check "ruby" "-v"
check "perl" "-v"
check "lua" "-v"
check "mysql" "--version"

'''
PenTest
'''

check "freedom" "-version"
# Security Scanner
check "nmap" "-V"

''' 
Text Editors
'''

check "nano" "--version"
if hash vi --version 2>/dev/null; then
  check "vi" "--version"
else
  check "vim" "--version"
fi
check "emacs" "--version"
check "code" "--version"
check "atom" "--version"

'''
File Editors
'''

# Office Suite
check "libreoffice" "--version"
# PDF Viewer
check "okular" "--version"
# Typesetting System
check "tex" "--version"
# 3D CAD Modeler
check "freecad" "--version"

'''
Window Managers
'''

check "i3" "--version"
# Partition Tables Manipulator

# TODO:""

check "parted" "--version"
# System Optimizer
check "stacer" "--version"
# BitTorrent Client
check "transmission-cli" "--version"

''' 
Media 
'''

# Multimedia Player/Framework
check "vlc" "--version"
# Audio Player
check "audacious" "--version"
# Graphics Editor
check "gimp" "--version"
# Entertainment Center
check "kodi" "--version"

'''
Browsers
'''

check "chromium" "--version"
check "firefox" "--version"

'''
Email Applications
'''

check "thunderbird" "--version"

# TODO: extend
