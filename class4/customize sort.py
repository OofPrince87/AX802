# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:17:40 2020

@author: seanw
"""

import random
from functools import cmp_to_key

datas = [[random.randrange(50),random.randrange(50)]]

def mysort(datas):
    for i in range(len(datas)-1):
        for j in range(len(datas)-1-i):
            if datas[j] > datas [j+1]:
                datas[j] , datas[j+1] = datas[j+1]
                
    
def myCMP(data1,data2):
    cmp1 = data1[0]+data1[1]*2
    cmp2 = data2[0]+data2[1]*2
    
    if cmp1 >cmp2:
        return 1