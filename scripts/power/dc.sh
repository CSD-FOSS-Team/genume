#!/bin/bash

configure find grep head cat
# Looks for all the power supplies.
dir=$(find /sys/ -name power_supply -type d 2> /dev/null)

# Distinguises the dc input and it assumes there is only one.
dir=$(grep -lire Mains $dir 2> /dev/null | head -n 1)
cnt=0
curdir=${dir%/*}

if [ -f ${curdir}/online ]; then
    online=$(cat ${curdir}/online)
    value connected2ac ${online}
fi
