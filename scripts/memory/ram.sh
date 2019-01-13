#!/bin/bash

totalMem=$(grep Mem /proc/meminfo | head -n 1 | cut -f 2 -d :)
freeMem=$(grep Mem /proc/meminfo | head -n 2 | tail -n 1 | cut -f 2 -d :)
swapMem=$(grep Mem /proc/meminfo | head -n 3 | tail -n 1 | cut -f 2 -d :)

echo VALUE BAS total_memory \" $totalMem \"
echo VALUE BAS free_memory \" $freeMem \"
echo VALUE BAS swap_memory \" $swapMem \"
