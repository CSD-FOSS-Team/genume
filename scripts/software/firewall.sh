#!/bin/bash

configure echo ufw grep cut
# Check for root user.
if [ "$EUID" -ne 0 ]; then

    value firewall "<requires root>"

else

    # TODO: Extend.

    status=$(sudo ufw status verbose)

    active=$(echo "$status" | grep Status: | cut -d " " -f 2)

    value firewall $active

fi
