#!/bin/bash

cat /proc/cpuinfo | grep name | head -n 1 | cut -d ":" -f 2

