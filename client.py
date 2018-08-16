import socket ,sys ,os
host = "192.168.150.128"
port = 5555

c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))
print 'Connected'
while True:
	data= c.recv(1024)
	print data
	send_data=raw_input('\nclient : ')
	c.send(send_data)
