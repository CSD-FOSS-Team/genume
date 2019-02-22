#!/bin/bash

configure cat grep head cut
model=$(cat /proc/cpuinfo | grep "model name" | head -n 1 | cut -d ":" -f 2)
vendor=$(cat /proc/cpuinfo | grep "vendor_id" | head -n 1 | cut -d ":" -f 2)

value model $model
value --advanced vendor $vendor
