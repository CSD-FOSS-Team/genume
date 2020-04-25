#!/bin/bash

configure grep head cut tail

totalMem=$(awk '( $1 == "MemTotal:" ) { print $2/1048576 }' /proc/meminfo)
cachedMem=$(awk '( $1 == "Cached:" ) { print $2/1048576 }' /proc/meminfo)
freeMem=$(awk '( $1 == "MemAvailable:" ) { print $2/1048576 }' /proc/meminfo)
swapMem=$(awk '( $1 == "SwapTotal:" ) { print $2/1048576 }' /proc/meminfo)
swapFreeMem=$(awk '( $1 == "SwapFree:" ) { print $2/1048576 }' /proc/meminfo)

value total_memory $totalMem GiB
value available_memory $freeMem GiB
value cached_memory $cachedMem GiB
value swap_memory $swapMem GiB
value swap_free_memory $swapFreeMem GiB
