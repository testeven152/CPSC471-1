
""" The server shall be invoked as:

python serv.py <PORTNUMBER>

<PORTNUMBER> specifies the port at which ftp server accepts connection requests.
For example: python serv.py 1234 """

import socket
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

def ls():
    print("ls")

def put():
    print("put")

def get():
    print("get")

# ------------------------

# Server port
portnum = sys.argv[1]

print("Port Number: " + portnum)

# create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to port
serverSocket.bind(('localhost',int(portnum)))

# start listening on socket
serverSocket.listen(5)


while True:

    print ("Waiting for connections...")

    # Accept connections
    client, addr = serverSocket.accept()

    print ("Accepted connection from client: ", addr)

    command = ''
    quit = 0
    while quit == 0:

        command = client.recv(4)

        if command == "get":
            client.send("SUCCESS\n")
            get()
        elif command == "put":
            client.send("SUCCESS\n")
            put()
        elif command == "ls":
            client.send("SUCCESS\n")
            ls()
        elif command == "quit":
            client.send("SUCCESS\n")
            quit = 1
        else:
            client.send("FAILURE\n")

    client.close()