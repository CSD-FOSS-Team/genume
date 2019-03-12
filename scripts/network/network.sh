#!/bin/bash

configure lspci lsusb egrep wc echo cat

wcnt=0
echo $wcnt > /tmp/wirelessgenume
ecnt=0
echo $ecnt > /tmp/ethernetgenume

lspci | egrep -i 'Network|Ethernet|802.11' | while read i
do
	wireless=''
	ethernet=''
	a=${i#*: }
	if [ $(echo $a | egrep -i "Wireless|802.11" | wc -l) -eq 1 ]; then
		wireless=$(echo $a)
		wcnt=$(cat /tmp/wirelessgenume)
		wcnt=$(($wcnt + 1))
		echo $wcnt > /tmp/wirelessgenume
		
	elif [ $(echo $a | grep -i "Ethernet" | wc -l) -eq 1 ]; then
		ethernet=$(echo $a)
		ecnt=$(cat /tmp/ethernetgenume)
		ecnt=$(($ecnt + 1))
		echo $ecnt > /tmp/ethernetgenume
	fi
	if [  ! -z "${wireless}" ]
	then
		subcat Wireless.Wireless_$wcnt
		value Wireless "${wireless}"
	elif [  ! -z "${ethernet}" ]
	then
		subcat Ethernet.Ethernet_$ecnt
		value Ethernet "${ethernet}"
	fi
done
lsusb | egrep -i "Network|Wireless|Ethernet|802.11" | while read i
do
	wireless=''
	ethernet=''
	a=${i#*: }
	if [ $(echo $a | egrep -i "Wireless|802.11" | wc -l) -eq 1 ]; then
		wireless=$(echo $a)
		wcnt=$(cat /tmp/wirelessgenume)
		wcnt=$(($wcnt + 1))
		echo $wcnt > /tmp/wirelessgenume
	elif [ $(echo $a | grep -i "Ethernet" | wc -l) -eq 1 ]; then
		ethernet=$(echo $a)
		ecnt=$(cat /tmp/ethernetgenume)
		ecnt=$(($ecnt + 1))
		echo $ecnt > /tmp/ethernetgenume
	fi

	if [  ! -z "${wireless}" ]
	then
		subcat Wireless.Wireless_$wcnt
		value Wireless "${wireless}"
	elif [  ! -z "${ethernet}" ]
	then
		subcat Ethernet.Ethernet_$ecnt
		value Ethernet "${ethernet}"
	fi
done
rm /tmp/wirelessgenume
rm /tmp/ethernetgenume
