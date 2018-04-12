#!/bin/bash

# Dependencies: lscpu

echo VALUE BAS threads $(lscpu | grep ^CPU\(s\): | cut -d: -f2)

echo VALUE ADV sockets $(lscpu | grep ^Socket\(s\): | cut -d: -f2)
echo VALUE ADV cores_per_socket $(lscpu | grep ^Core\(s\)\ per\ socket: | cut -d: -f2)
echo VALUE ADV threads_per_core $(lscpu | grep ^Thread\(s\)\ per\ core: | cut -d: -f2)
