
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
		tmpBuff = sock.recv(numBytes)
		
		# The other side has closed the socket
		if not tmpBuff:
			break
		
		# Add the received bytes to the buffer
		recvBuff += tmpBuff
	
	return recvBuff

def newsocket():
    newsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    newsocket.bind(('',0))
    port = newsocket.getsockname()[1]
    client.send(str(port))
    newsocket.listen(1)
    return newsocket

def get():
    tempsocket = newsocket()
    linkTemp, linkAddr = tempsocket.accept()

    fileName = linkTemp.recv(1024)
    fileObj = open(fileName, "r")
    
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
                    numSent += linkTemp.send(fileData[numSent:])
            
            # The file has been read. We are done
            else:
                break
    
    fileSize = linkTemp.recv(1024)

    fileObj.close()
    linkTemp.close()

    print "File Name: " , fileName
    print "Size: " , fileSize

def put():
    tempsocket = newsocket()
    linkTemp, linkAddr = tempsocket.accept()

    fileName = linkTemp.recv(1024)
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
    fileSize = int(len(fileSizeBuff))
	
	# Get the file data
    fileData = recvAll(linkTemp, fileSize)
	
    fileObj.write(fileData)

    print "File Name: " , fileName
    print "Size: ", fileSize
		
    fileObj.close()
    linkTemp.close()

def ls():
    tempsocket = newsocket()
    directory = ''
    linkTemp, linkAddr = tempsocket.accept()

    # Run ls command, get output, and print it
    for line in commands.getstatusoutput('ls -l'):
        directory = str(line) + '\n'

    #send directory back to client
    linkTemp.send(directory)

    linkTemp.close()

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