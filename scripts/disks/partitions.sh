#!/bin/bash

num=$(lsblk | wc -l)
echo VALUE BAS number_of_devices $[$num - 1]
for ((i=2;i<=num;i++))
do
	name=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 1 -d ' ')
	maj=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 2 -d ' ' | cut -f 1 -d :)
	min=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 2 -d ' ' | cut -f 2 -d :)
	mountpoint=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 7 -d ' ')
	read_only=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 5 -d ' ')
	removable=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 3 -d ' ')
	size=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 4 -d ' ')
	type=$(lsblk | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 6 -d ' ')
	echo VALUE BAS name_$[$i - 1] \"$name\"
	echo VALUE BAS major_device_number_$[$i - 1] \"$maj\"
	echo VALUE BAS minor_device_number_$[$i - 1] \"$min\"
	echo VALUE ADV mountpoint_$[$i - 1] \"$mountpoint\"
	echo VALUE ADV read_only_$[$i - 1] \"$read_only\"
	echo VALUE ADV removable_$[$i - 1] \"$removable\"
	echo VALUE ADV size_$[$i - 1] \"$size\"
	echo VALUE ADV type_$[$i - 1] \"$type\"
done
