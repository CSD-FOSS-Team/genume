#!/bin/bash

configure getconf grep expr sed wc

oput=$(getconf -a | grep CACHE)

# get the sizes lines with non zero values and then keep only the name
names=$(<<< "$oput" grep _SIZE | grep -v '0$' | sed 's/_SIZE.*//')

value number_of_caches $(<<< "$names" wc -l)
value number_of_cache_levels $(<<< "$names" sed 's/_.*//' | uniq | wc -l)

for name in $names; do
    norm_name="$(echo $name | tr '[:upper:]' '[:lower:]')"
    subcat $norm_name

    value size "$(($(<<< "$oput" grep "$name"_SIZE | sed 's/^.* [^0-9]*//') / 1024)) KiB"
    value line_size $(<<< "$oput" grep "$name"_LINESIZE | sed 's/^.* [^0-9]*//')
    value ways_of_associativity $(<<< "$oput" grep "$name"_ASSOC | sed 's/^.* [^0-9]*//')
done
