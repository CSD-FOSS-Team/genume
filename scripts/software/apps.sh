#!/bin/bash


# check for a app and if exists provide the version
function check {
	name=$1
	version=$2

	# add the prefix app_ to every entry
	key="app_$name"

	if command -v "$name" > /dev/null; then

		echo VALUE BAS "$key" \"$($name $version 2>&1 | head -n1)\"
	else
		echo VALUE BAS "$key" \""<not found>"\"	
	fi
}


check "bash" "-version"
check "make" "--version"
check "git" "--version"

check "gnome-software" "--version"

check "gcc" "--version"
check "java" "-version"
check "python" "-V"
check "mysql" "--version"
check "freedom" "-version"

# TODO extend

