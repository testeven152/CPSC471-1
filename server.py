
""" The server shall be invoked as:

python serv.py <PORTNUMBER>

<PORTNUMBER> specifies the port at which ftp server accepts connection requests.
For example: python serv.py 1234 """

import socket
import sys
import commands

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

def tempsocket():
    

def get():
    print("get")

def put():
    tempsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tempsocket.bind(('',0))
    port = tempsocket.getsockname()[1]
    client.send(str(port))
    tempsocket.listen(1)
    linkTemp, linkAddr = tempsocket.accept()

    fileName = connTemp.recv(1024)
    fileObj = open(fileName, 'wb')

    # The buffer to all data received from the
	# the client.
    fileData = ""
	
	# The temporary buffer to store the received
	# data.
    recvBuff = ""
	
	# The size of the incoming file
    fileSize = 0	
	
	# The buffer containing the file size
    fileSizeBuff = ""
	
	# Receive the first 10 bytes indicating the
	# size of the file
    fileSizeBuff = recvAll(linkTemp, 10)
		
	# Get the file size
    fileSize = int(fileSizeBuff)
	
	# Get the file data
    fileData = recvAll(linkTemp, fileSize)
	
    fileObj.write(fileData)

    print "File Name: ", fileName
    print "Size in bytes: ", fileSize
		
	# Close our side
    fileObj.close()
    linkTemp.close()

def ls():
    tempsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tempsocket.bind(('', 0))
    port = tempsocket.getsockname()[1]
    client.send(str(port))
    tempsocket.listen(1)
    directory = ''
    linkTemp, linkAddr = tempsocket.accept()

    # Run ls command, get output, and print it
    for line in commands.getstatusoutput('ls -l'):
        directory = str(line) + '\n'

    #send directory back to client
    linkTemp.send(directory)

    linkTemp.close()

if len(sys.argv) != 2:
    print("Invalid arguments")
    sys.exit()

# Server port
portnum = sys.argv[1]

print("Port Number: " + portnum)

# create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to port
serverSocket.bind(('localhost', int(portnum)))

# start listening on socket
serverSocket.listen(5)

while 1:

    print ("Listening...")

    # Accept connections
    client, addr = serverSocket.accept()

    print ("Connected.")

    command = ''
    while 1:

        command = client.recv(4)

        if command == "get":
            client.send("SUCCESS")
            get()
        elif command == "put":
            client.send("SUCCESS")
            put()
        elif command == "ls":
            client.send("SUCCESS")
            ls()
        elif command == "quit":
            client.send("SUCCESS")
            break
        else:
            client.send("FAILURE")

    client.close()