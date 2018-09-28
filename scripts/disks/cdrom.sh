#!/bin/bash

num=$(awk '{print NF}' /proc/sys/dev/cdrom/info | head -n 3 | tail -n 1)
num=$[ $num - 2 ]
echo GROUP BAS cdroms
echo VALUE BAS connected_cdrom_devices ${num}

if (($num > 0))
then	
	for i in $num
	do
	two=$[ $i + 2 ]
	three=$[ $i + 3 ]
	four=$[ $i + 4 ]
		drive_name=$(cat /proc/sys/dev/cdrom/info | head -n 3 | tail -n 1 | tr -s '\t' ' ' | cut -f $two -d ' ')
		drive_speed=$(cat /proc/sys/dev/cdrom/info | head -n 4 | tail -n 1 | tr -s '\t' ' ' | cut -f $two -d ' ')
		number_of_slots=$(cat /proc/sys/dev/cdrom/info | head -n 5 | tail -n 1 | tr -s '\t' ' ' | cut -f $four -d ' ')
		closes_tray=$(cat /proc/sys/dev/cdrom/info | head -n 6 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		opens_tray=$(cat /proc/sys/dev/cdrom/info | head -n 7 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		locks_tray=$(cat /proc/sys/dev/cdrom/info | head -n 8 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		changes_speed=$(cat /proc/sys/dev/cdrom/info | head -n 9 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		plays_audio=$(cat /proc/sys/dev/cdrom/info | head -n 14 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		writes_cdr=$(cat /proc/sys/dev/cdrom/info | head -n 15 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		writes_cdrw=$(cat /proc/sys/dev/cdrom/info | head -n 16 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		reads_dvd=$(cat /proc/sys/dev/cdrom/info | head -n 17 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		writes_dvdr=$(cat /proc/sys/dev/cdrom/info | head -n 18 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		writes_dvdram=$(cat /proc/sys/dev/cdrom/info | head -n 19 | tail -n 1 | tr -s '\t' ' ' | cut -f $three -d ' ')
		if (($closes_tray > 0))
		then
			closes_tray=true
		else
			closes_tray=false
		fi
		if (($opens_tray > 0))
		then
			opens_tray=true
		else
			opens_tray=false
		fi
		if (($locks_tray > 0))
		then
			locks_tray=true
		else
			locks_tray=false
		fi
		if (($changes_speed > 0))
		then
			changes_speed=true
		else
			changes_speed=false
		fi
		if (($plays_audio > 0))
		then
			plays_audio=true
		else
			plays_audio=false
		fi
		if (($writes_cdr > 0))
		then
			writes_cdr=true
		else
			writes_cdr=false
		fi
		if (($writes_cdrw > 0))
		then
			writes_cdrw=true
		else
			writes_cdrw=false
		fi
		if (($reads_dvd > 0))
		then
			reads_dvd=true
		else
			reads_dvd=false
		fi
		if (($writes_dvdr > 0))
		then
			writes_dvdr=true
		else
			writes_dvdr=false
		fi
		if (($writes_dvdram > 0))
		then
			writes_dvdram=true
		else
			writes_dvdram=false
		fi
		
		echo PATH BAS cdroms.cdrom_$i
		echo VALUE BAS drive_name \"$drive_name\"
		echo VALUE ADV drive_speed \"$drive_speed\"
		echo VALUE ADV number_of_slots \"$number_of_slots\"
		echo VALUE ADV closes_tray \"$closes_tray\"
		echo VALUE ADV opens_tray \"$opens_tray\"
		echo VALUE ADV locks_tray \"$locks_tray\"
		echo VALUE ADV changes_speed \"$changes_speed\"
		echo VALUE ADV plays_audio \"$plays_audio\"
		echo VALUE ADV writes_cdr \"$writes_cdr\"
		echo VALUE ADV writes_cdrw \"$writes_cdrw\"
		echo VALUE ADV reads_dvd \"$reads_dvd\"
		echo VALUE ADV writes_dvdr \"$writes_dvdr\"
		echo VALUE ADV writes_dvdram \"$writes_dvdram\"
	done
fi 

