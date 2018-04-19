#!/bin/bash
TOTAL=$(grep MemTotal /proc/meminfo|awk {'print $2'})
TOTAL_SWAP=$(grep SwapTotal /proc/meminfo|awk {'print $2'})

echo VALUE BAS memory_total $TOTAL
echo VALUE BAS memory_swap $TOTAL_SWAP
