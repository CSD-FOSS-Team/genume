#!/bin/bash


#looks for all the power supplies
dir=$(find /sys/ -name power_supply -type d 2>/dev/null)

#distinguises the dc input and it assumes there is only one
dir=$(grep -lire Mains $dir 2>/dev/null | head -n 1)
cnt=0
echo $dir
curdir=${dir%/*}

if [ -f ${curdir}/online ]
then
	online=$(cat ${curdir}/online)
	echo VALUE BAS online ${online}
fi
