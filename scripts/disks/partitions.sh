#!/bin/bash

num=$(lsblk | wc -l)
echo PATH BAS partitions
echo VALUE BAS number_of_devices $[$num - 1]
for ((i=2;i<=num;i++))
do
	name=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 1 -d ' ' | sed 's/[^a-zA-Z0-9]//g')
	maj=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 2 -d ' ' | cut -f 1 -d :)
	min=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 2 -d ' ' | cut -f 2 -d :)
	mountpoint=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 7 -d ' ')
	read_only=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 5 -d ' ')
	removable=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 3 -d ' ')
	size=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 4 -d ' ')
	type=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 6 -d ' ')
	
	echo PATH BAS partitions.partition_$[$i - 1]
	echo VALUE BAS name \"$name\"
	echo VALUE ADV major_device_number \"$maj\"
	echo VALUE ADV minor_device_number \"$min\"
	echo VALUE ADV mountpoint \"$mountpoint\"
	echo VALUE ADV read_only \"$read_only\"
	echo VALUE ADV removable \"$removable\"
	echo VALUE BAS size \"$size\"
	echo VALUE ADV type \"$type\"
done
