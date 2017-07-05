#Alice

import time

import messenger as m
import threading

#tb = threading.Thread()

#tb.start()

#tb.join()


p = 23
g = 5
a = 6
A = g**a % p
j = 0
message2 = 0



while j == 0:
   m.PutMessage(str(A))
   time.sleep(15)
   message2 = str(m.GetMessage())
   print('received' + message2)
   if message2 != 0:
       j = 1
        
B = float(message2)
        
s = B**a % p

#Bob

import time
import messenger as m
import threading

ta = threading.Thread()

ta.start()

ta.join()


p = 23
g = 5
b = 15
B = g**b % p
j = 0
message2 = 0



while j == 0:
   m.PutMessage(str(B))
   time.sleep(15)
   message2 = str(m.GetMessage())
   print('received' + message2)
   if message2 != 0:
       j = 1

A = float(message2)        
s = A**b % p
