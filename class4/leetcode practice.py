# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:58:00 2020

@author: seanw
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = sorted(s)
        
        t = sorted(t)
        
        '''
        for i in range(len(s)-1):
            for j in range(len(s)-1-i):
                if s[j] > s[j+1]:
                    s[j],s[j+1] = s[j+1].s[j]
                    
        
        for i in range (len(t)-1):
            for j in range(len(t)-1-i):
                if t[j] > t[j+1]:
                    t[j],t[j+1] = t[j+1].t[j]
        '''                                        
                    
        if s == t:
            return True
        
        else:
            return False
        
s = "wrrew"
t = "fefef"

ans = Solution().isAnagram(s,t)

print (ans)


    
    