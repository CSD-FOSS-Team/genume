#!/bin/bash

GpuName=$(lspci | grep "VGA compatible" | head -n 1)
GpuName="${GpuName##*:}"

echo VALUE BAS gpu_model \"$GpuName\"
