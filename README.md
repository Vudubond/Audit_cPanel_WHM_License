# Audit_cPanel-WHM_License
Python program to audit cPanel/WHM license

This is a Python program to audit cPanel/WHM license. The CSV file can be exported from the cPanel license managing interface.

The program checks if the IP is up, then checks the hostname and the hostname in CSV file are the same.  Create files active_ips, inactive_ips and ip_hostname_mismatch to write the outputs. The program will create the files in the present working directory. Please update the hostname in the license portal as well in the server for improved results. 

Verify if the IP is offline if listed in the file inactive_ips. Review the licenses of the IPs listed in the file ip_hostname_mismatch and update their hostnames in the cPanel interface as well. 
