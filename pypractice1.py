# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:30:10 2019

@author: Abhishek
"""

ar = [1,-2,3,4,5]
def sum(ar):
    for i in range(0,5):
        if ar[i] >= 0 :
            t = pow(int(ar[i]),3)
            print(t)
    return 0
sum(ar)
