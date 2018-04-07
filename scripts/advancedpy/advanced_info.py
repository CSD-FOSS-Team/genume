# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 02:58:23 2018
Written in python 3.4.2
Script for finding infos of your box
1.Try to find basic programs installed in the system
-gcc, perl, python, nmap, netcat, wget, ftp
2. Find fles that have the sticky bit
3. Find files with the name passwords
4. 



Libraries used
--------------
os,subprocess,grp,pwd

Calls to external programs
--------------------------
awk

Run with the foloowing order
find_distro()
find_version()
find_cpu('True')
find_mem('True')  
disks()
find_desktop_enviroment()
users()


"""