
""" The ftp client is invoked as:

cli <server machine> <server port>

<server machine> is the domain name of the server (ecs.fullerton.edu). This will be
converted into 32 bit IP address using DNS lookup. For example: python cli.py ecs.fullerton.edu 1234

Upon connecting to the server, the client prints out ftp>, which allows the user to run the 
following commands.

ftp> get <file name> (downloads file <file name> from the server)
ftp> put <filename> (uploads file <file name> to the server)
ftp> ls(lists files on the server)
ftp> quit (disconnects from the server and exits)
 """

import socket
import sys

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

def newsocket(serveraddr_):
    port = int(clientSocket.recv(5))
    newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    newsocket.connect((serveraddr_, int(port)))
    return newsocket

def get(file, server):
    tempsocket = newsocket(server)
    tempsocket.send(file)
    fileObj = open(file, 'wb')
    fileData = ""
    recvBuff = ""
    fileSize = 0
    fileSizeBuff = ""
    fileSizeBuff = recvAll(tempsocket, 10)
    fileSize = int(fileSizeBuff)
    fileData = recvAll(tempsocket, fileSize)
    fileObj.write(fileData)
    tempsocket.send(str(fileSize))
    fileObj.close()
    tempsocket.close()


def put(file, server):
    tempsocket = newsocket(server)
    tempsocket.send(file)
    fileObj = open(file, "r")
    numSent = 0
    fileData = None

    while True:
        # Read 65536 bytes of data
        fileData = fileObj.read(65536)
        
        # Make sure we did not hit EOF
        if fileData:
            
                
            # Get the size of the data read
            # and convert it to string
            dataSizeStr = str(len(fileData))
            
            # Prepend 0's to the size string
            # until the size is 10 bytes
            while len(dataSizeStr) < 10:
                dataSizeStr = "0" + dataSizeStr
        
        
            # Prepend the size of the data to the
            # file data.
            fileData = dataSizeStr + fileData	
            
            # The number of bytes sent
            numSent = 0
            
            # Send the data!
            while len(fileData) > numSent:
                numSent += tempsocket.send(fileData[numSent:])
        
        # The file has been read. We are done
        else:
            break

    fileObj.close()
    tempsocket.close()

def ls(server):

    tempsocket = newsocket(server)

    directory = tempsocket.recv(1024)

    print(directory)

    tempsocket.close()

# Server address
serverAddr = sys.argv[1]

# Server port
serverPort = sys.argv[2]

print("Server Address: " + serverAddr)
print("Port Number: " + serverPort)

# this creates the TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client socket connects to address at port
clientSocket.connect((serverAddr, int(serverPort)))

command = ''

while 1: 

    #print ftp> and ask user for command
    command = raw_input('ftp> ')

    if 'get' in command:
        clientSocket.send("get")
        print(clientSocket.recv(8))
        get(command[4:], serverAddr)
    elif 'put' in command:
        clientSocket.send("put")
        print(clientSocket.recv(8))
        put(command[4:], serverAddr)
    elif command == "ls":
        clientSocket.send("ls")
        print(clientSocket.recv(8))
        ls(serverAddr)
    elif command == "quit":
        clientSocket.send("quit")
        print(clientSocket.recv(7))
        break
    else:
        clientSocket.send("fail")
        print(clientSocket.recv(8))

# close connection
clientSocket.close()
