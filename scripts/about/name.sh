#!/bin/bash

# Get the path of the script.
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

configure date git awk sort cut sed
value genume Graphical ENUMEration ver. 1.0
value team CSD foss team, https://foss.csd.auth.gr

# Test changing values.
value date "$(date)"

# Show off contributors.
while IFS="" read -r p || [ -n "$p" ]; do
  value authors "$p"
done < "$DIR/AUTHORS.txt"
