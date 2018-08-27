import socket
import struct
import binascii

s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

while True:

	packet = s.recvfrom(2048)
	ethhead = packet[0] [0:14]
	eth = struct.unpack("!6s6s2s",ethhead)

	print "+++++ Ethernet Frame +++++"
	print "Destination MAC :",binascii.hexlify(eth[0])
	print "Source MAC :",binascii.hexlify(eth[1])
	binascii.hexlify(eth[2])

	ipheader = packet[0][14:34]
	iphdr = struct.unpack("!BBHHHBBH4s4s",ipheader)
	
	print "+++++ IP +++++"
	print "TTL :", iphdr[5]
	print "Protocol Number :", iphdr[6]
	print "Source IP :", socket.inet_ntoa(iphdr[9])
	print "Destination IP :", socket.inet_ntoa(iphdr[8])
	
