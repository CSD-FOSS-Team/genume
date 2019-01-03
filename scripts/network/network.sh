#!/bin/bash

wcnt=0
ecnt=0
echo PATH BAS Ethernet
echo PATH BAS Wireless
lspci | egrep -i 'Network|Ethernet|802.11' | while read i
do
	a=${i#*: }
	if [ $(echo $a | egrep -i "Wireless|802.11" | wc -l) -eq 1 ]; then
		wireless=$(echo $a)
		name=${wireless}
		wcnt=$[ $wcnt + 1]
	elif [ $(echo $a | grep -i "Ethernet" | wc -l) -eq 1 ]; then
		ethernet=$(echo $a)
		name=${ethernet}
		ecnt=$[ $ecnt + 1]
	fi
	
	if [  ! -z "${wireless}" ]
	then
		echo PATH BAS Wireless.Wireless_$[$wcnt]
		echo VALUE BAS Wireless \"${wireless}\"
	elif [  ! -z "${ethernet}" ]
	then
		echo PATH BAS Ethernet.Ethernet_$[$ecnt]
		echo VALUE BAS Ethernet \"${ethernet}\"
	fi
done

lsusb | egrep -i "Network|Wireless|Ethernet|802.11" | while read i
do
	a=${i#*: }
	if [ $(echo $a | egrep -i "Wireless|802.11" | wc -l) -eq 1 ]; then
		wireless=$(echo $a)
		name=${wireless}
		wcnt=$[ $wcnt + 1]
	elif [ $(echo $a | grep -i "Ethernet" | wc -l) -eq 1 ]; then
		ethernet=$(echo $a)
		name=${ethernet}
		ecnt=$[ $ecnt + 1]
	fi

	if [  ! -z "${wireless}" ]
	then
		echo PATH BAS Wireless.Wireless_$[$wcnt]
		echo VALUE BAS Wireless \"${wireless}\"
	elif [  ! -z "${ethernet}" ]
	then
		echo PATH BAS Ethernet.Ethernet_$[$ecnt]
		echo VALUE BAS Ethernet \"${ethernet}\"
	fi
done
