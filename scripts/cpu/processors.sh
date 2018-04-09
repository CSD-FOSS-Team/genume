#!/bin/bash

threads=$(cat /proc/cpuinfo | grep processor | wc -l)
echo "KVAL thread_count \"${threads}\""

