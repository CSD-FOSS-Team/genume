#!/bin/bash

configure lsblk wc head tail tr cut sed
cache=$(lsblk)
num=$(echo "$cache" | wc -l)
subcat partitions
value number_of_devices $(($num - 1))
for ((i = 2; i <= num; i++)); do
    name=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 1 -d ' ' | sed 's/[^a-zA-Z0-9]//g')
    maj=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 2 -d ' ' | cut -f 1 -d :)
    min=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 2 -d ' ' | cut -f 2 -d :)
    mountpoint=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 7 -d ' ')
    read_only=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 5 -d ' ')
    removable=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 3 -d ' ')
    size=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 4 -d ' ')
    type=$(echo "$cache" | head -n $i | tail -n 1 | tr -s '\t' ' ' | cut -f 6 -d ' ')

    subcat partitions.partition_$(($i - 1))
    value name $name
    value --advanced major_device_number $maj
    value --advanced minor_device_number $min
    value --advanced mountpoint $mountpoint
    value --advanced read_only $read_only
    value --advanced removable $removable
    value size $size
    value --advanced type $type
done
