import socket
import threading

bindip = "192.168.150.128"
port = 5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((bindip,port))

s.listen(1)

print "[*] Listeing on %s:%d" % (bindip,port)
conn, client = s.accept()
print client

print "connected"
while True:
	data= s.recv(1024)
	print data
	server_send=raw_input('\nserver : ')
	conn.send(server_send)
	s.close()
