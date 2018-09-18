#! /bin/bash

sudo lshw > hardware.txt 
##whatis lshw : lists hardware 
##              needs root privileges
##              password must be entered
##whatis hardware.txt : output of lshw 
##                      info is read from 

l11Size=$( grep *-cache -A 7 hardware.txt | grep size | head -n 1 | cut -f 2 -d : )
l2Size=$( grep *-cache -A 7 hardware.txt | grep size | head -n 2 | tail -n 1 | cut -f 2 -d : )
l12Size=$( grep *-cache -A 7 hardware.txt | grep size | head -n 3 | tail -n 1 | cut -f 2 -d : )

rm hardware.txt

echo VALUE BAS L1i Size \" $l11Size \"
echo VALUE BAS L1d Size \" $l12Size \"
echo VALUE BAS L2  Size \" $l2Size  \"
