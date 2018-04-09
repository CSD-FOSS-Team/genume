#!/bin/sh

model=$(cat /proc/cpuinfo | grep name | head -n 1 | cut -d ":" -f 2)
echo "KVAL cpu_model \"${model}\""

