#!/bin/bash


echo VALUE BAS genume 'Graphical\ ENUMeration\ ver.\ 1.0' 
echo VALUE BAS Team 'CSD\ foss\ team,\ https://foss.csd.auth.gr' 
# testing list values 
git log --pretty="VALUES BAS authors \"%an %ce\"" | sort | uniq | grep -v noreply

# testing changing values
echo VALUE BAS date \"$(date)\"
