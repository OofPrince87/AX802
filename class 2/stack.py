# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:53:47 2020

@author: seanw
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        

class stack:
    
    def __init__(self):
        self.head = Node(1)
        
    def trace(self):
        run = self.head.next
        while run:
            print(run.value)
            run = run.next
            
    def push(self,value):
        run = self.head
        while run.next:
            run = run.next
        
        run.next = Node(value)
        
    def pop(self):
        pre = self.head
        run = self.head.next
        
        while run.next:
            pre = pre.next
            run = run.next
            
        pre.next = None
        
        
        return run.value
    
    
    
MyList = stack
    
        