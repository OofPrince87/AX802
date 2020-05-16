# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:38:20 2020

@author: seanw
"""

import stack


class linkinglist:
    
    def __init__(self):
       self.head = node(10)
       
    def trace(self):
        run = self.head.next
        while run != None:
            print(run.value)
            run = run.next
            
    def append(self,value):
        run = self.head
        while run.next != None:
            run = run.next
        run.next = node(value)
        
        
        



class node:
    def __init__(self,value):
        self.value = value
        self.next = None
'''       
MyList = linkinglist()

MyList.trace()

for i in range(101):
    MyList.append(1)
    
MyList.trace()
'''

Mystack = stack.stack()

Mystack.push(3)

for i in range(4):
    Mystack.push(1)
'''    
Mystack.trace()
'''

for i in range(4):
    print(Mystack.pop())
        
'''
a = node(10)



a.next = node(20)
a.next.next = node(30)
a.next.next.next = node(40)
a.next.next.next.next = node(50)
a.next.next.next.next.next = node(60)


run = a

while run.next != None :
    run = run.next
run.next = node(70)
    
    
    
run = a
while run != None:
    print(run.value)
    run = run.next
'''    