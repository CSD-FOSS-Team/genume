#!/bin/bash

configure lspci grep head

# Pripary gpu.
GpuName=$(lspci | grep "VGA compatible" | head -n 1)
GpuName="${GpuName##*:}"
value gpu_model $GpuName

# Secondary gpu on hybrid systems.
GpuName=$(lspci | grep "3D" | head -n 1)
GpuName="${GpuName##*:}"
value 3d_accel $GpuName