import socket ,sys ,os
import threading

host = "192.168.73.129"
port = 5555

c= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))
print 'Now Connected'

def send():
	while True:
		send_data=raw_input('\nclient : ')
		c.send(send_data)
def rec():
	while True:
		s_data= c.recv(1024)
		print "Server: %s" % s_data

thread_send = threading.Thread(target = send)
thread_send.start()

thread_rec = threading.Thread(target = rec)
thread_rec.start()	

