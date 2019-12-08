# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:16:46 2019

@author: Abhishek
"""
s1=0
s2=0
ar = [1,2,3,4,5]
s1=0
s2=0
for i in range(0,5):
    if ar[i]>s1:
        s2=s1
        s1=ar[i]
    elif ar[i]<s1 and ar[i]>s2:
        s2=ar[i]
print(s2)