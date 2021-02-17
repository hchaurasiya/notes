#!/bin/python3

import sys
import socket
from datetime import datetime 

#input - python3 port_scanner.py <ip> 

if (len(sys.argv) == 2):
	target = socket.gethostbyname(sys.argv[1]) #translates a host name to ipv4
else:
	print("Invalid amount of arguments")
	print("Syntax: python3 port_scanner.py <ip>")
	sys.exit()
#adding a banner
print("-"*50)
print("Scanning target %s"%target)
print("Time started: "+str(datetime.now()))
print("-"*50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is ipv4 and SOCK_STREAM is port
		socket.setdefaulttimeout(1) #this is a float value
		result = s.connect_ex((target,port)) #returns 0 is there is no error on connection else returns an error
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()

except socket.gaierror:#couldn't connect to the hostname
	print("Hostname couldn't be resolved")
	sys.exit()
	
except socket.error:
	print("Couldn't connect to server")
	sys.exit()
	
