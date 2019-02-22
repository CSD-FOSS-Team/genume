#!/bin/bash

configure cat grep cat
# Looks for all the storage devices.
dir=$(cat /proc/partitions | grep -E -o '\<[s][r][[:alpha:]]*[0-9]\>|\<[s][d][[:alpha:]]*\>|\<[h][d][[:alpha:]]*\>')

cnt=0
# Counts the storage devices.
for i in $dir; do
    cnt=$(($cnt + 1))
done
subcat disks
value connected_storage_devices ${cnt}

for i in $dir; do
    subcat disks.disk_$i
    par=$(cat /proc/partitions | grep -o $i[0-9])
    partitions=0
    for j in $par; do
        partitions=$((partitions + 1))
    done
    if [ -f /sys/class/block/$i/device/model ]; then
        model=$(cat /sys/class/block/$i/device/model)
        value model $model
    fi
    if [ -f /sys/class/block/$i/device/vendor ]; then
        vendor=$(cat /sys/class/block/$i/device/vendor)
        value --advanced vendor $vendor
    fi
    if [ -f /sys/class/block/$i/size ]; then
        size=$(cat /sys/class/block/$i/size)
        value size $size blocks
    fi
    if (($partitions > 0)); then
        value partitions $partitions
    fi
done
