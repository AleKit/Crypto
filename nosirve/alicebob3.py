#archivo socket.py

#https://pymotw.com/2/socket/tcp.html

#All of the examples are run on OS X and Linux, and those systems are 
#usually configured to know that the name "localhost" refers to 127.0.0.1.

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
        
#------------------------        
#archivo alice.py

import socket
import sys

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
    
    data = sock.recv(0)
    if data[0] == 'B':
        message2 = data[1:]
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
    
        
B = float(message2)   
s = B**a % p
print s

#------------------------
#archivo bob.py

import socket
import sys

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
    print >>sys.stderr, 'Alice sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    
    data = sock.recv(0)
    if data[0] == 'A':
        message2 = data[1:]
        print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

A = float(message2)        
s = A**b % p
print s
