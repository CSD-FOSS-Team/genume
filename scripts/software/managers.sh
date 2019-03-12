#!/bin/bash

# The script self handles dependencies
configure

subcat software_managers

name="pacman"
if command -v "$name" > /dev/null; then
    value "$name" "$(pacman -Q pacman | awk {'print $2'})"
    value --advanced "${name}_pkgs"  "$(pacman -Q | wc -l)"
    if command -v "checkupdates" > /dev/null; then
        value --advanced "${name}_outdated"  "$(checkupdates | wc -l)"
    fi
    value --advanced "${name}_explicit"  "$(pacman -Qe | wc -l)"
    value --advanced "${name}_deps"  "$(pacman -Qd | wc -l)"
    value --advanced "${name}_orphans"  "$(pacman -Qdt | wc -l)"
    value --advanced "${name}_unofficial"  "$(pacman -Qm | wc -l)"
fi

name="yum"
if command -v "$name" > /dev/null; then
    value "$name" "$version"
    if command -v rpm > /dev/null; then
        value --advanced "${name}_pkgs"  "$(rmp -qa |wc -l)"
    fi
fi

name="apt"
if command -v "$name" > /dev/null; then
    value "$name" "$version"
    if command -v dpkg > /dev/null; then
        value --advanced "${name}_pkgs"  "$(dpkg -l| grep -c '^i')"
    fi
fi
