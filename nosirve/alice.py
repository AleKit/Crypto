# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:31:42 2016

@author: usupclab-18
"""
#intento de comunicacion con ZMQ, Diffie-Hellman

#Alice

import zmq, time
from datetime import datetime

context = zmq.Context()

#create this node as publisher
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:25648")




p = 23
g = 5
a = 6
A = g**a % p
j = 0
message2 = 0

context2 = zmq.Context()
socket2 = context2.socket(zmq.SUB)
socket2.connect("tcp://localhost:25647")

#filter message for particular subscriber ('1')
socket2.setsockopt(zmq.SUBSCRIBE, '1')

while j == 0:
   message = str(A)
   print str(datetime.now().time()) + "> sending: A = " + message
   socket.send(message)
   time.sleep(15)
   message2 = socket2.recv()
   print(str(datetime.now().time()) + "> received: B = " + str(message2))
   if message2 != 0:
       j = 1
        
B = float(message2)
        
s = B**a % p
