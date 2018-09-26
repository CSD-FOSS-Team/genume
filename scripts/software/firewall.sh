#!/bin/bash

# check for root user
if [ "$EUID" -ne 0 ]; then

	echo VALUE BAS firewall \""<requires root>"\"

else

	# TODO extend

	status=$(sudo ufw status verbose)

	active=$(echo "$status" | grep Status: | cut -d " " -f 2)

	echo VALUE BAS firewall \"$active\"
	
fi

