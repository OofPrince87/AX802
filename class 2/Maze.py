# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:01:14 2020

@author: seanw
"""

MAZE = [[1,1,1,1,1,1,1,1,1,1],
        [0,1,0,0,0,1,1,1,0,0],
        [1,0,0,1,1,0,0,1,0,0],
        [1,0,0,1,0,0,1,1,0,0],
        [1,0,1,1,1,0,0,1,0,0],
        [1,0,0,1,0,1,0,1,0,0],
        [1,0,0,1,1,0,0,1,1,0],
        [1,0,0,1,1,0,0,1,0,0],
        [1,0,0,1,0,0,0,1,0,0],
        [1,0,0,1,1,0,1,1,0,1]]

START = [1,1]
END = [9,9]

#---------------------------------#


visited = [[0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0]]

PathStack = [START[0],START[1]]


def run(x,y):
    if (x,y) == END:
        print("have been reach end")
        print(PathStack)
        
    
    if x+1 < len(MAZE[0]) and MAZE[x+1][y] == 0 and visited[x+1][y] == 0:
        visited [x+1][y] = 1
        run(x+1,y)
    if x-1 <= len(MAZE[0]) and MAZE[x-1][y] == 0 and visited[x-1][y] == 0:
        visited [x-1][y] = 1
        run(x-1,y)
    if y+1 < len(MAZE[0]) and MAZE[x][y+1] == 0 and visited[x][y+1] == 0:
        visited [x][y+1] = 1
        run(x,y+1)
        
    if y-1 <= len(MAZE[0]) and MAZE[x][y-1] == 0 and visited[x][y-1] == 0:
        visited [x][y-1]
        run(x,y-1)
        


run(START[0],START[1])

        
        
    



