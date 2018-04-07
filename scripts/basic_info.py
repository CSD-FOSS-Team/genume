# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 02:58:23 2018
Written in python 3.4.2
Script for finding basic infos of your box
1.distro
2.kernel version
3.cpu info  [two options print all or less information]
4.memory    [two options print all or less information]
5.disks 
6.desktop enviroments
7.print all the users of the system 

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

def find_string(s,string,a,b):
    s=str(s)
    start = s.find(string) 
    if start!=-1:
        return s[start+a:start+len(string)-b]
    else:
        return 'error'

def find_distro():  
    Distro = ['/ubuntu/','/debian/','linuxmint','/archlinux/']    
    with open("/etc/apt/sources.list","r") as myfile:
        data=myfile.readlines()
        for i in Distro:
            F = find_string(data,i,1,1)
            if F!= 'error':
                print ("{0}: {1}".format("Linux distro" , F))
                
def find_version():         
    with open("/proc/version","r") as myfile:
        data=myfile.readlines()
        for line in data:
            print ("{0}: {1}".format("kernel version", line))

def find_desktop_enviroment():    
    import os,subprocess
    A= os.listdir("/usr/share/xsessions")
    print('installed desktops:')
    print('--------------------')
    for i in A:
        print(i)
    cmd='echo $DESKTOP_SESSION'
    B=subprocess.check_output(cmd, shell=True)  
    print("{0}: {1}".format("now you use",B.decode('utf-8') ))
    
    
def find_mem(all):
    import subprocess   
    print('Memory:')
    print('--------------------')
    if all=='True':  
        cmd = '''awk '$3=="kB"{$2=$2/1048576;$3="GB"} 1' /proc/meminfo | column -t'''
        B=subprocess.check_output(cmd, shell=True)
        B=B.decode('utf-8')
        print(B)
    if all=='False':
        i = 0
        j=0
        string = 'MemTotal','MemFree','MemAvailable','SwapTotal'
        with open('/proc/meminfo',"r") as myfile:
            data=myfile.readlines()
            while j<=3:
                while i<len(data):
                    if data[i].find(string[j])!=-1:
                        print(data[i])
                        break
                    i+=1
                j+=1    
                
                
def find_cpu(all):
    import subprocess   
    print('Cpu:')
    print('--------------------')
    if all=='True':  
        cmd = 'lscpu'
        B=subprocess.check_output(cmd, shell=True)
        B=B.decode('utf-8')
        print(B)
    if all=='False':
        i = 0
        j=0
        string = 'model name','cpu cores','Thread(s) per core',\
        'CPU MHz','CPU max MHz', 'cache size','model',\
        'vendor_id','Architecture','cpu MHz',\
        'Thread(s) per core','SwapTotal',
        
        with open('/proc/cpuinfo',"r") as myfile:

            data=myfile.readlines()
            while j<=len(string)-1:
                while i<=len(data)-1:
                    if data[i].find(string[j])!=-1:
                        print(data[i])
                        break
                    i+=1
                j+=1    
                                
            
def disks():
    import subprocess   
    print('Disk space:')
    print('--------------------')
    cmd='df -T'
    B=subprocess.check_output(cmd, shell=True)  
    print(B.decode('utf-8') )
    
def users():
    import pwd, grp
    print('users:')
    print('--------------------')
    for p in pwd.getpwall():
        print("{0}:{1} \n{2}:{3}\n".format("user",p[0], "group",grp.getgrgid(p[3])[0]))
    

find_distro()
find_version()
find_cpu('False')
find_mem('False')  
disks()
find_desktop_enviroment()
users()