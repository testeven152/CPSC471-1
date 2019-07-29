
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
