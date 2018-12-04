#!/bin/bash


# check for a app and if exists provide the version
function check {
	name=$1
	version=$2

	# add the prefix app_ to every entry
	key="app_$name"

	if command -v "$name" > /dev/null; then
		echo VALUE BAS "$key" \"$($name $version 2>&1 | head -n2)\" GROUP "apps"
	else
		echo VALUE BAS "$key" \""<not found>"\"	GROUP "missing_apps"
	fi
}


check "bash" "-version"
check "make" "--version"
check "git" "--version"

check "gnome-software" "--version"

check "gcc" "--version"
check "java" "-version"
check "python" "-V"
check "ruby" "-v"
check "perl" "-v"
check "mysql" "--version"
check "freedom" "-version"
check "nmap" "-V"
check "nano" "--version"
check "vi" "--version"
check "emacs" "--version"
check "libreoffice" "--version"

# TODO extend

