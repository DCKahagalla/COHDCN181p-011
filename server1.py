import socket ,sys ,os
from threading import Thread

bindip = sys.argv[1]
port=int(sys.argv[2])
#port = 5555

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((bindip,port))

s.listen(2)

conn, addr = s.accept()

print addr, "Now Connected"

def send():
	while True:
		data=raw_input('\nServer : ')
		conn.send(data)
def rec():
	while True:
		s_data= s.recv(1024)
		print "Client: %s" % s_data

thread_send = threading.Thread(target = send)
thread_send.start()

thread_rec = threading.Thread(target = rec)
thread_rec.start()	









