#!/bin/bash

configure date git awk sort cut sed
value genume Graphical ENUMEration ver. 1.0
value team CSD foss team, https://foss.csd.auth.gr

# Test changing values.
value date $(date)

# Test list values.
git log --all --format="VALUE BAS authors \"%aN <%aE>\"" | awk '{ print length, $0 }' | sort -nur | cut -d" " -f2- | sort -u -t'<' -k2,2 | sed '/noreply/s/ <.*>//' | sort
