
""" The server shall be invoked as:

python serv.py <PORTNUMBER>

<PORTNUMBER> specifies the port at which ftp server accepts connection requests.
For example: python serv.py 1234 """

import socket
import commands
import sys

# ------- Functions -------
def recvAll(sock, numBytes):

	# The buffer
	recvBuff = ""
	
	# The temporary buffer
	tmpBuff = ""
	
	# Keep receiving till all is received
	while len(recvBuff) < numBytes:
		
		# Attempt to receive bytes
		tmpBuff =  sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff

def ls()

def put(fileName)

def get(fileName)

# ------------------------

# Server port
portnum = sys.argv[1]

print("Port Number: " + portnum)

# create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to port
serverSocket.bind(('localhost'),int(portnum))

# start listening on socket
serverSocket.listen(5)


