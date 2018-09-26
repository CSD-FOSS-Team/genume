#!/bin/bash


totalMem=$(grep Mem /proc/meminfo | head -n 1 | cut -f 2 -d : )
freeMem=$(grep Mem /proc/meminfo | head -n 2 | tail -n 1 | cut -f 2 -d : )
swapMem=$(grep Mem /proc/meminfo | head -n 3 | tail -n 1 | cut -f 2 -d : )

echo GROUP BAS ram
echo VALUE BAS memory_total \" $totalMem \"
echo VALUE BAS memory_free \" $freeMem \"
echo VALUE BAS memory_swap \" $swapMem \"
