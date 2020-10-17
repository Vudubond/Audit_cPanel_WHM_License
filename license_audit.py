#!/usr/bin/python

import os
import socket
import csv

#specify csv file name
csv_file_name = '/root/test/csv'

#create output files if not existing
dir = os.getcwd()
active_ips = dir + '/active_ips'
inactive_ips = dir + '/inactive_ips'
ip_hostname_mismatch = dir + '/ip_hostname_mismatch'

if not os.path.exists(active_ips):
    os.mknod(active_ips)

if not os.path.exists(inactive_ips):
    os.mknod(inactive_ips)

if not os.path.exists(ip_hostname_mismatch):
    os.mknod(ip_hostname_mismatch)

#read the csv file for IP and hostname
f = open(csv_file_name)
csv_file = csv.reader(f)

for row in csv_file:
    ip = row[1]
    hostname = row[2].lower()

#check if IP is up
    response = os.system("ping -c 1 " + ip + " 2>&1 >/dev/null")
    if response == 0:
        pass
#      print ip, 'is up!'

    else:
#      print ip, 'is down!'
        f = open("inactive_ips", "a+")
        f.write(ip + "\n")
        f.close()
        continue

#get the hostname from the IP
    try:
        host = socket.gethostbyaddr(ip)[0].lower()
    except socket.herror:
        pass
#   print "==========================="
#   print host
#   print hostname
#   print "==========================="

#compare hostname of the IP and the hostname from the CSV file
#if hostname matches, write to the file active_ips
    if host == hostname :
        f = open("active_ips", "a+")
        f.write(ip + "\n")
        f.close()

#if the hostname doesn't match write to the file ip_hostname_mismatch
    else:
        f = open("ip_hostname_mismatch", "a+")
        f.write(ip + "\n")
        f.close()

f.close()
