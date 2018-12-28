#!/bin/bash

function check {
	name=$1

	# add the prefix app_ to every entry
	key="app_$name"

	if command -v "$name" > /dev/null; then
		echo VALUE BAS "$name" \""<found>"\" GROUP "software_managers"
        else
		echo VALUE BAS "$name" \""<not found>"\" GROUP "software_managers"
	fi
}

check "pacman"
check "apt"
check "yum"
