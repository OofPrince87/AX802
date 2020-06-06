# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:25:03 2020

@author: seanw
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
        
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

'''
def DFS(node:Node):
    if not node:
        return
    
    print(node.value)
    DFS(node.left)
    DFS(node.right)
    
DFS(root)
'''

def bfs(root):
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        if node.right:
            queue.append(node.right)
            
        if node.left:
            queue.append(node.left)
            
        print(node.value)
        
bfs(root)