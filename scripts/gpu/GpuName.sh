#!/bin/bash

Manufacter=$(glxinfo| grep "OpenGL vendor string"| head -n 1|cut -d ":" -f 2)
GpuName=$(glxinfo| grep "OpenGL renderer string"| head -n 1|cut -d ":" -f 2)


echo VALUE BAS Gpu Manufacter\"$Manufacter\"
echo VALUE BAS Gpu Model\"$GpuName\"
