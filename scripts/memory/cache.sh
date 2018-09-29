#! /bin/bash

oput=$( getconf -a | grep CACHE )
sizes=$( grep _SIZE <<< "$oput" )
i=0
j=0
k=0
numOfCaches=0
for size in $sizes
do
	if [ $( expr $k % 2 ) -eq 0 ]
	then
		strings[$i]=$size
		let i=$( expr $i + 1 )
	else
		nums[$j]=$( expr $size / 1024 )
		let j=$( expr $j + 1 )
	fi
	let k=$( expr $k + 1 )
done
l=0
for s in ${strings[*]}
do
	if [ ${nums[$l]} -eq 0 ]
	then
		echo VALUE BAS $s \" does not exist \"
	else
		numOfCaches=$( expr $numOfCaches + 1 )
		echo VALUE BAS $s \" ${nums[$l]} \"
	fi	
	let l=$( expr $l + 1 )
done
echo VALUE BAS numOfCaches \" $numOfCaches \"
unset sizes
unset strings
unset nums
linesizes=$( grep _LINESIZE <<< "$oput" )
i=0
j=0
k=0
for size in $linesizes
do
	if [ $( expr $k % 2 ) -eq 0 ]
	then
		strings[$i]=$size
		let i=$( expr $i + 1 )
	else
		nums[$j]=$size
		let j=$( expr $j + 1 )
	fi
	let k=$( expr $k + 1 )
done
l=0
for s in ${strings[*]}
do
	if [ ${nums[$l]} -eq 0 ]
	then
		echo VALUE ADV $s \" doesnt exist \"
	else
		echo VALUE ADV $s \" ${nums[$l]} \"
	fi
	let l=$( expr $l + 1 )
done
unset linesizes
unset strings
unset nums
i=0
j=0
k=0
l=0
assocs=$( grep _ASSOC <<< "$oput" )
for val in $assocs
do
	if [ $( expr $k % 2) -eq 0 ]
	then
		strings[$i]=$val
		let i=$( expr $i + 1 )
	else
		nums[$j]=$val
		let j=$( expr $j + 1 )
	fi
	let k=$(expr $k + 1 )
done
for s in ${strings[*]}
do
	if [ ${nums[$l]} -eq 0 ]
	then 
		echo VALUE ADV $s \" doesnt exist \"
	else 
		echo VALUE ADV $s \" ${nums[$l]}
	fi
	let l=$( expr $l + 1 )
done
