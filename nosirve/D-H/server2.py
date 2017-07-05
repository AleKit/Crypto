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
            return data
        except:
            print "Error"
        finally:
            print 'no more data from', add
            
            
def send_info(datalist,conn,add):
    if datalist != []:
        print 'sending data back to the client'
        for item in datalist:
            conn.sendall(item)
            time.sleep(3)
    else:
        print 'no more data (from)', add
        #break
        #except:
        #    print "Error"

def server():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 4444)
    print 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(2)
    ta = []
    i=0
    datalist = []
    listconn = []
    listaddr = []

    while True:
        # Wait for a connection
        print 'waiting for a connection'
        connection, client_address = sock.accept()
        listconn.append(connection)
        listaddr.append(client_address)

        try:
            print 'connection from', client_address

            #thread.start_new_thread(accepted_client, (connection, client_address))
            #accepted_client(connection, client_address)
            #ta.append(threading.Thread(target=accepted_client(connection, client_address)))
            #data=ta[i].start()
            #print(data)
            #ta[i].join()
            data = connection.recv(16)
            print 'received "%s"' % data
            if data != []:
                datalist.append(data)
                print(datalist)
                i=i+1
            if i > 1:
                print(listconn)
                conn1 = listconn[0]
                conn2 = listconn[1]
               # for j in range(2):
                    #threading.Thread(target=send_info(datalist,listconn[j],listaddr[j]))
                for item in datalist:
                        
                    conn1.send(item)
                    conn2.send(item)
                    time.sleep(3)
                    #send_info(datalist,listconn[j],listaddr[j])
            
        finally:
            # Clean up the connection
            connection.close()
