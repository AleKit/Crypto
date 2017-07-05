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
        data = sock.recv(4096)
        if data[0] == 'B':
            message2 = data[1:]
            print >>sys.stderr, 'received "%s"' % data
            
    except:
        message2 = 16.5
    finally:
        print >>sys.stderr, 'closing socket'
        sock.close()


        B = float(message2)
        s = B**a % p
        print s

