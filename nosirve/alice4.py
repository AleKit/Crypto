# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:38:49 2016

@author: usupclab-227
"""

import socket
import sys

def alice():
    p = 23
    g = 5
    a = 6
    A = g**a % p



   # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)

    try:

    # Send data
        message = 'A' + str(A)
        print >>sys.stderr, 'Alice sending "%s"' % message
        sock.sendall(message)

    # Look for the response
        while True:
            data = sock.recv(16)
            if data[0] == 'B':
                message2 = data[1:]
                print >>sys.stderr, 'received "%s"' % data
                break
            
    except:
        message2 = 16.5
    finally:
        print >>sys.stderr, 'closing socket'
        


        B = float(message2)
        s = B**a % p
        print s
        
        sock.close()