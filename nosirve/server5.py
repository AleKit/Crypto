#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:20:32 2016

@author: Ale
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:40:48 2016
@author: usupclab-227
"""

#archivo socket.py

#https://pymotw.com/2/socket/tcp.html

#All of the examples are run on OS X and Linux, and those systems are
#usually configured to know that the name "localhost" refers to 127.0.0.1.

import socket
#import sys

import thread
import threading

import time

def accepted_client(conn, add):
    print "Start"
    while True:
        try:
            data = conn.recv(16)
            print 'received "%s"' % data
            if data:
                print 'sending data back to the client'
                conn.sendall(data)
                time.sleep(10)
            else:
                print 'no more data from', add
                break
        except:
            print "Error"

def server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 10000)
    print 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)
    ta = []
    i=0

    while True:
        # Wait for a connection
        print 'waiting for a connection'
        connection, client_address = sock.accept()

        try:
            print 'connection from', client_address

            #thread.start_new_thread(accepted_client, (connection, client_address))
            #accepted_client(connection, client_address)
            ta.append(threading.Thread(target=accepted_client(connection, client_address)))
            ta[i].start()
            ta[i].join()
            i=i+1
            
        finally:
            # Clean up the connection
            connection.close()