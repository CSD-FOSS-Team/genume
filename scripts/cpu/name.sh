#!/bin/bash

model=$(cat /proc/cpuinfo | grep "model name" | head -n 1 | cut -d ":" -f 2)
vendor=$(cat /proc/cpuinfo | grep "vendor_id" | head -n 1 | cut -d ":" -f 2)

echo VALUE BAS model \"$model\"
echo VALUE ADV vendor \"$vendor\"
