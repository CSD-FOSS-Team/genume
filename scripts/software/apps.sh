#!/bin/bash


# check for a app and if exists provide the version
function check {
	name=$1
	version=$2

	# add the prefix app_ to every entry
	key="app_$name"

	if command -v "$name" > /dev/null; then
		echo VALUE BAS "$key" \"$($name $version 2>&1 | sed '/./q; d')\" GROUP "apps"
	else
		echo VALUE BAS "$key" \""<not found>"\"	GROUP "missing_apps"
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
check "vi" "--version"
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
check "parted" "--version"
check "stacer" "--version"
check "transmission-cli" "--version"
check "vlc" "--version"
check "audacious" "--version"
check "gimp" "--version"
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