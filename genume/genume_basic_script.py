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
8.Basic network informations (local ip, public ip, ifconfig)
 
For checking the connectivity we ping 8.8.8.8 (google dns server)
For finding the public ip we use the website 'ipinfo.io'

Python Libraries used
--------------------------
os,subprocess,grp,pwd

Bash Libraries used
--------------------------
awk,ping,curl,netstat

Run with the following order
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
    print()
    with open("/etc/apt/sources.list","r") as myfile:
        data=myfile.readlines()
        for i in Distro:
            F = find_string(data,i,1,1)
            if F!= 'error':
                return ("{0}: {1}".format("Linux distro" , F))

def find_version():    
    def ver():
        with open("/proc/version","r") as myfile:
            data=myfile.readlines()
            for line in data:
                return ("{0}: {1}".format("kernel version", line))     

    with open("/proc/sys/kernel/hostname","r") as host:
        for line in host:
            return ("{0}: {1}\n{2}".format("computer name", line,ver()))
            
def find_desktop_enviroment():    
    import os,subprocess
    A= os.listdir("/usr/share/xsessions")
    L=[]
    for i in A:
        L.append(i)
    cmd='echo $DESKTOP_SESSION'
    B=subprocess.check_output(cmd, shell=True)  
    return ("{0}: {1}\n{2}: {3}".format("installed",L,"*now you use",B.decode('utf-8') ))
   
    
def find_mem(all):
    import subprocess   
    if all=='True':  
        cmd = '''awk '$3=="kB"{$2=$2/1048576;$3="GB"} 1' /proc/meminfo | column -t'''
        B=subprocess.check_output(cmd, shell=True)
        B=B.decode('utf-8')
        return B
    if all=='False':
        i = 0
        j=0
        string = 'MemTotal','MemFree','MemAvailable','SwapTotal'
        with open('/proc/meminfo',"r") as myfile:
            data=myfile.readlines()
            while j<=len(string)-1:
                while i<len(data):
                    if data[i].find(string[j])!=-1:
                        print(data[i])
                        break
                    i+=1
                j+=1    
                
                
def find_cpu(all):
    import subprocess   
    #print('Cpu:')
    #print('--------------------')
    if all=='True':  
        cmd = 'lscpu|column -x'
        B=subprocess.check_output(cmd, shell=True)
        B=B.decode('utf-8')
        #print(B)
        return B
    if all=='False':
        i = 0
        j=0
        string = 'model name','cpu cores','Thread(s) per core',\
        'CPU MHz','CPU max MHz', 'cache size','model',\
        'vendor_id','Architecture','cpu MHz',\
        'Thread(s) per core','SwapTotal',
        D=[]
        with open('/proc/cpuinfo',"r") as myfile:

            data=myfile.readlines()
            while j<=len(string)-1:
                while i<=len(data)-1:
                    if data[i].find(string[j])!=-1:
                        D.append(data[i])
                        break
                    i+=1
                j+=1    
        D=[D[i] for i in range(len(D))]
        print(D)
        return 
                                
#find_cpu('False')
          
def disks():
    import subprocess   
    cmd='df -T'
    B=subprocess.check_output(cmd, shell=True)  
    return B.decode('utf-8')


        
def users():
    import pwd, grp, subprocess

    cmd1='''awk -F: '($3 >= 1000){print($1,$3)}' /etc/passwd | column -t'''
    B1=subprocess.check_output(cmd1, shell=True)
    print(B1.decode('utf-8'))
    cmd2='echo $USER'
    B2=subprocess.check_output(cmd2, shell=True)
    return ("{0}:\n{1}  {2}: {3}".format("users",B1.decode('utf-8'), "\ncurrent user",B2.decode('utf-8') ))
        
    #for p in pwd.getpwall():
    #    print("{0}:{1} \n{2}:{3}\n".format("user",p[0], "group",grp.getgrgid(p[3])[0]))

def local_ip():
    import os,subprocess
    cmd1 ='''ip r | grep src | cut -d ' ' -f 12'''
    B1=subprocess.check_output(cmd1, shell=True)
    cmd2 = '''ping -q -w 1 -c 1 8.8.8.8 > /dev/null && echo ok || echo error'''
    B2=subprocess.check_output(cmd2, shell=True)
    cmd3 ='curl ipinfo.io/ip'
    B3=subprocess.check_output(cmd3, shell=True)
    return ("{0}: {1}  {2}? {3}".format("local ip",B1.decode('utf-8'), "\nonline",B2.decode('utf-8')))

def public_ip():
    import os,subprocess
    cmd2 = '''ping -q -w 1 -c 1 8.8.8.8 > /dev/null && echo ok || echo error'''
    B2=subprocess.check_output(cmd2, shell=True)
    if B2==b'ok\n':
        cmd3 ='curl ipinfo.io/ip'
        B3=subprocess.check_output(cmd3, shell=True)    
        return ("{0}: {1}".format("public ip",B3.decode('utf-8')))
    else:
        return ("you are not online")

def ifconfig():
    import os,subprocess
    cmd2 = '/sbin/ifconfig -a'
    B2=subprocess.check_output(cmd2, shell=True)
    return ("{0}: {1}".format("netwrok interfaces",B2.decode('utf-8')))
    
def open_ports():
    import os,subprocess
    cmd='''netstat -tuwanp|awk -F: '/:::/ && /LISTEN/ {print($4)}' '''
    B = subprocess.check_output(cmd, shell=True)
    return ("{0}\n{1}".format("Open ports",B.decode('utf-8')))
    
def installed_programs():   
    import os,subprocess
    cmd='''ls -alh /usr/bin/|awk '{print $9}' '''
    B = subprocess.check_output(cmd, shell=True)
    return ("{0}\n{1}".format("installed programs",B.decode('utf-8')))
     
def installed_programs2():   
    import os,subprocess
    cmd='which perl'
    B = subprocess.check_output(cmd, shell=True)
    cmd1='which gcc'
    B1 = subprocess.check_output(cmd1, shell=True)
    cmd2='which nc'
    B2 = subprocess.check_output(cmd2, shell=True)
    cmd3='which python'
    B3 = subprocess.check_output(cmd3, shell=True)
    cmd4='which wget'
    B4 = subprocess.check_output(cmd4, shell=True)
    cmd5='mysql --version'
    B5 = subprocess.check_output(cmd5, shell=True)
    cmd6='which java'
    B6 = subprocess.check_output(cmd6, shell=True)
    return ("{0}: {1}\n{2}: {3}\n{4}: {5}\
    \n{6}: {7}\n{8}: {9}\n{10}: {11}\n{12}: {13}".format("Perl",B.decode('utf-8'),\
    "GCC",B1.decode('utf-8'),\
    "python",B3.decode('utf-8'),\
    "netcat",B2.decode('utf-8'),\
    "wget",B4.decode('utf-8'),\
    "mysql",B5.decode('utf-8'),\
    "Java",B6.decode('utf-8')))

    
def passwd():
    import os,subprocess
    cmd='cat /etc/passwd'
    B = subprocess.check_output(cmd, shell=True)
    return("{0}".format(B.decode('utf-8'))) 

    
def about():
    string1 ='genome version 1.0'
    string2 ='Licence: GPL v.?'
    string3 ='website'
    return("{0}\n{1}\n{2}".format(string1,string2,string3))    
    

