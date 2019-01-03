#!/bin/bash

lspci | egrep -i 'Network|Ethernet' | while read i
do
        a=${i#*: }
	if [ $(echo $a | grep -i "Wireless" | wc -l) -eq 1 ]; then
		wireless=$(echo $a)
		name=${wireless}
	elif [ $(echo $a | grep -i "Ethernet" | wc -l) -eq 1 ]; then
	        ethernet=$(echo $a)
		name=${ethernet}
	fi
	
	if [  ! -z "${wireless}" ]
	then
		echo VALUE BAS wireless \"${wireless}\"
	elif [  ! -z "${ethernet}" ]
	then
		echo VALUE BAS ethernet \"${ethernet}\"
	fi
done

echo VALUE BAS wireless \""This is another wireless adapter"\"
