
#messenger.py

import Queue
 
MessageQueue1 = Queue.Queue()
MessageQueue2 = Queue.Queue()
 
def GetMessage1():
    return MessageQueue1.get()
 
def PutMessage1(message):
    MessageQueue1.put(message)
    return
    
def GetMessage2():
    return MessageQueue2.get()
 
def PutMessage2(message):
    MessageQueue2.put(message)
    return
    
#Alice

import time
import messenger as m
#import threading
#import bob

#tb = threading.Thread()

#tb.start()

#tb.join()

def ali():
    p = 23
    g = 5
    a = 6
    A = g**a % p
    j = 0
    message2 = 0


    while j == 0:
        m.PutMessage1(str(A))
        #time.sleep(7)
        message2 = str(m.GetMessage2())
        print('received ' + message2)
        if message2 != 0:
            j = 1
        
    B = float(message2)   
    s = B**a % p
    return s
    
ali()

#Bob

import time
import messenger as m
import threading

def bo():

    p = 23
    g = 5
    b = 15
    B = g**b % p
    j = 0
    message2 = 0


    while j == 0:
        m.PutMessage2(str(B))
        time.sleep(7)
        message2 = str(m.GetMessage1())
        print('received ' + message2)
        if message2 != 0:
            j = 1

    A = float(message2)        
    s = A**b % p
    
bo()
