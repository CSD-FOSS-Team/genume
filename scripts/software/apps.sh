#!/bin/bash

# Check for an app and if it exists provide the version.
function check() {
  name=$1
  version=$2

  key=$name

  if command -v "$name" >/dev/null; then
    echo VALUE BAS "$key" \"$($name $version 2>&1 | sed '/./q; d')\" GROUP "apps"
  fi
}

'''
Shells.
'''

check "bash" "-version"
check "zsh" "--version"
check "csh" "--version"
check "ksh" "--version"
check "fish" "--version"

'''
Code Helpers.
'''

# Shell Parser, Formatter and Interpreter.
check "shfmt" "--version"
# Regex Evaluator.
check "kiki" "--version"
# Flash Card Tool to Help Memorize Shortcuts.
check "mnemosyne" "--version"
# Fix Previous Command.
check "thefuck" "--version"
# Hex Editor.
check "ghex" "--version"
# GUI Diff.
check "meld" "--version"
# Code Indexing.
check "ctags" "--version"
# Code Search (a specialized grep).
check "ack" "--version"

'''
Terminal Management.
'''

# Terminal Multiplexer.
check "byobu" "--version"
# Another Terminal Multiplexer.
check "tmux" "--version"
# Multiple Terminals Management.
check "terminator" "--version"

'''
# TODO:
'''

# Executes Commands in Makefile.
check "make" "--version"

'''
Version Control.
'''

check "git" "--version"
check "subversion" "--version"

'''
GNOME.
'''

check "gnome-software" "--version"

'''
KDE.
'''

check "kde-applications" "--version"
# Bulk rename.
check "krename" "--version"
# File-version control.
check "kdiff" "--version" 

'''
Programming Languages & Compilers.
'''

# GNU Compiler Collection (C, C++, Go...).
check "gcc" "--version"
check "java" "-version"
check "python" "-V"
# Haskell Compiler.
check "ghci" "--version"
check "ruby" "-v"
# Ruby version control.
check "rvm" "--version"
# Another Ruby Version Manager.
check "rbenv" "--version"
check "perl" "-v"
check "lua" "-v"
check "mysql" "--version"

'''
PenTest.
'''

check "freedom" "-version"
# Security Scanner.
check "nmap" "-V"
# Wire protocols inspector.
check "wireshark-cli" "--version"

'''
Remote Connectivity.
'''

check "ssh" "-V"
# Uses FUSE to mount folders remotely using SSH.
check "sshfs" "--version"
# FTP Client.
check "filezilla" "--version"
# Cross-Platform Multiple Computers Control.
check "synergy" "--version"
# Sync Dir-Trees in Multiple Systems.
check "unison" "--version"
# Dropbox Alternative.
check "sparkleshare" "--version"

'''
Encryption.
'''

check "veracrypt" "--version"
check "pgp" "--version"
check "gpg" "--version"

''' 
Text Editors/IDEs.
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
check "sublime" "--version"
check "netbeans" "--version"
check "eclipse" "--version"
check "kate" "--version"
check "codelite" "--version"
check "gedit" "--version"
check "geany" "--version"
check "kwrite" "--version"
check "scite" "--version"

'''
Virtual Enviroment Testing.
'''

check "vagrant" "--version"
check "docker" "--version" 

'''
File Editors.
'''

# Text-Based File Manager.
check "ranger" "--version"
# Office Suite.
check "libreoffice" "--version"
# PDF Viewer.
check "okular" "--version"
# Another PDF Viewer.
check "zathura" "--version"
# Typesetting System.
check "tex" "--version"
# Diagrams Creator.
check "dia" "--version"
# Plots Creator.
check "gnuplot" "--version"
# 3D CAD Modeler.
check "freecad" "--version"

'''
Window Managers.
'''

check "i3" "--version"

'''
# TODO:
'''

# Partition Tables Manipulator.
check "parted" "--version"
# Command Line System Monitor.
check "htop" "--version"
# System Optimizer.
check "stacer" "--version"
# BitTorrent Client.
check "transmission-cli" "--version"

''' 
Media.
'''

# CD/DVD Burner.
check "k3b" "--version"
# Multimedia Player/Framework.
check "vlc" "--version"
# Graphics Editor.
check "gimp" "--version"

'''
IRC & General Communication.
'''

# Communication Wrapper.
check "pidgin" "--version"
# IRC Client.
check "hexchat" "--version"

'''
Browsers.
'''

check "chromium" "--version"
check "firefox" "--version"

'''
Email Applications.
'''

check "thunderbird" "--version"

# TODO: Extend.