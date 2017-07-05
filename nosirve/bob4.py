# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:40:29 2016

@author: usupclab-227
"""

import socket
import sys

def bob():
    p = 23
    g = 5
    b = 15
    B = g**b % p

   # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)

    try:

    # Send data
        message = 'B' + str(B)
        print >>sys.stderr, 'Bob sending "%s"' % message
        sock.sendall(message)
        print >>sys.stderr, 'probando1'

    # Look for the response
        while True:
            print('probando2')
            data = sock.recv(16)
            print >>sys.stderr, 'datos' % data
            if data[0] == 'A':
                message2 = data[1:]
                print >>sys.stderr, 'received "%s"' % data
                break
            
    except:
        print >>sys.stderr, 'no se ha recibido mensaje'
        message2 = 16.5
    finally:
        A = float(message2)
        s = A**b % p
        print s
        print >>sys.stderr, 'closing socket'
        sock.close()
