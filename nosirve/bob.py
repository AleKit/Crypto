# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 11:45:00 2016

@author: usupclab-18
"""

#Bob

import zmq, time
from datetime import datetime

context = zmq.Context()

#create this node as publisher
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:25647")




p = 23
g = 5
b = 15
B = g**b % p
j = 0
message2 = 0

context2 = zmq.Context()
socket2 = context2.socket(zmq.SUB)
socket2.connect("tcp://localhost:25648")

#filter message for particular subscriber ('1')
socket2.setsockopt(zmq.SUBSCRIBE, '1')

while j == 0:
   message = str(B)
   print str(datetime.now().time()) + "> sending: B = " + message
   socket.send(message)
   time.sleep(15)
   message2 = socket2.recv()
   print(str(datetime.now().time()) + "> received: A = " + str(message2))
   if message2 != 0:
       j = 1

A = float(message2)        
s = A**b % p
