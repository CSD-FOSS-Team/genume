#!/bin/bash

Manufacter=$(glxinfo| grep "OpenGL vendor string"| head -n 1|cut -d ":" -f 2)
GpuName=$(glxinfo| grep "OpenGL renderer string"| head -n 1|cut -d ":" -f 2)
OpenGLVersion=$(glxinfo|grep "OpenGL version"| head -n 1|cut -d ":" -f 2)

echo VALUE BAS Gpu Model\"$Manufacter\"
echo VALUE BAS Gpu Model\"$GpuName\"
echo VALUE ADV OpenGl Version \"$OpenGLVersion\"