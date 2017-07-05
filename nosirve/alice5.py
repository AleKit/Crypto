#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:19:23 2016

@author: Ale
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:38:49 2016
@author: usupclab-227
"""

import socket
import sys
import time

def alice():
    p = 23
    g = 5
    a = 6
    A = g**a % p
    i = 0



   # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    sock.connect(server_address)
    while True:
        try:
    
        # Send data
            message = 'A' + str(A)
            print >>sys.stderr, 'Alice sending "%s"' % message
            sock.sendall(message)
            time.sleep(2)
    
        # Look for the response
    
            data = sock.recv(16)
            if data[0] == 'B':
                message2 = data[1:]
                print >>sys.stderr, 'received "%s"' % data
                break
                
        except:
            print >>sys.stderr, 'no se ha recibido mensaje'
            message2 = -0.5
            i = i+1
            time.sleep(0.5)
            if i == 50:
                print >>sys.stderr, 'demasiados intentos'
                break
        finally:
            print >>sys.stderr, 'closing socket'
            sock.close()
        


    B = float(message2)
    s = B**a % p
    print s
        
        