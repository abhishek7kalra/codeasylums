# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:03:44 2019

@author: Abhishek
"""

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(i,5):
        print(k+1,end="")
    print("\n")