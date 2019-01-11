#!/bin/bash


echo VALUE BAS genume 'Graphical\ ENUMEration\ ver.\ 1.0' 
echo VALUE BAS team 'CSD\ foss\ team,\ https://foss.csd.auth.gr'

# testing changing values
echo VALUE BAS date \"$(date)\"

# testing list values
git log --all --format="VALUES BAS authors \"%aN <%aE>\"" | awk '{ print length, $0 }' | sort -nur | cut -d" " -f2- | sort -u -t'<' -k2,2 | sed '/noreply/s/ <.*>//' | sort