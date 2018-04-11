#!/bin/bash

processors=$(cat /proc/cpuinfo | grep processor | wc -l)

echo VALUE BAS processors $processors
