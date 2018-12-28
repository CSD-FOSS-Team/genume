#!/bin/bash

name="pacman"
if command -v "$name" > /dev/null; then
        echo VALUE BAS "$name" \""$(pacman -Q pacman | awk {'print $2'})"\" GROUP "software_managers"
        echo VALUE ADV "${name}_pkgs"  \""$(pacman -Q | wc -l)"\" GROUP "software_managers"
        if command -v "checkupdates" > /dev/null; then
                echo VALUE ADV "${name}_outdated"  \""$(checkupdates | wc -l)"\" GROUP "software_managers"
        fi
        echo VALUE ADV "${name}_explicit"  \""$(pacman -Qe | wc -l)"\" GROUP "software_managers"
        echo VALUE ADV "${name}_deps"  \""$(pacman -Qd | wc -l)"\" GROUP "software_managers"
        echo VALUE ADV "${name}_orphans"  \""$(pacman -Qdt | wc -l)"\" GROUP "software_managers"
        echo VALUE ADV "${name}_unofficial"  \""$(pacman -Qm | wc -l)"\" GROUP "software_managers"
else
        echo VALUE BAS "$name" \""<not found>"\" GROUP "software_managers"
fi

name="yum"
if command -v "$name" > /dev/null; then
        echo VALUE BAS "$name" \""$version"\" GROUP "software_managers"
else
        echo VALUE BAS "$name" \""<not found>"\" GROUP "software_managers"
fi

name="apt"
if command -v "$name" > /dev/null; then
        echo VALUE BAS "$name" \""$version"\" GROUP "software_managers"
else
        echo VALUE BAS "$name" \""<not found>"\" GROUP "software_managers"
fi
