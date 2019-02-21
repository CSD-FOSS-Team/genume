#!/bin/bash

# Dependencies: lscpu.
configure lscpu grep cut

value threads $(lscpu | grep ^CPU\(s\): | cut -d: -f2)

value --advanced sockets $(lscpu | grep ^Socket\(s\): | cut -d: -f2)
value --advanced cores_per_socket $(lscpu | grep ^Core\(s\)\ per\ socket: | cut -d: -f2)
value --advanced threads_per_core $(lscpu | grep ^Thread\(s\)\ per\ core: | cut -d: -f2)
