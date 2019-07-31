
""" The server shall be invoked as:

python serv.py <PORTNUMBER>

<PORTNUMBER> specifies the port at which ftp server accepts connection requests.
For example: python serv.py 1234 """

import socket
import sys

# Server port
portnum = sys.argv[1]

print("Port Number: " + portnum)

# create server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to port
serverSocket.bind(('localhost'),int(portnum))

# start listening on socket
serverSocket.listen(5)


