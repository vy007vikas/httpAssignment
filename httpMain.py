import sys    #to exit and to take parameters
import socket   #to use sockets in the program

#---->1---->creating a new socket
try:
	#create a new AF_INET socket
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error, msg:
	print 'Failed to create a new socket. Error code ' + str(msg[0]) + '. Error msg ' + str(msg[1])
	sys.exit();

#---->2---->checking the host name
#declaring host name to be the parameter recieved
host = sys.argv[1]
try:
	#getting the ip address of the host name
	ip_addr = socket.gethostbyname(host)
except socket.gaierror:
	#could not resolve
	print 'Hostname could not be resolved'
	sys.exit();

#---->3---->connection to the remote server
port = 80
s.connect((ip_addr,port))
print 'Socket connected to ' + host + ' on ip ' + ip_addr

#---->4---->preapare the message to be sent to the server
message = "HEAD / HTTP/1.1\r\n\r\n"
try:
	#send the whole string
	s.sendall(message)
except socket.error:
	#sending failed
	print 'Communication failed.'
	sys.exit()

#---->5---->Receiving the data
reply = s.recv(4096)
print reply

#---->6---->Closing the connection
s.close()
