# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:44:17 2019

@author: Abhishek
"""

n = int(input("enter number"))
num=0
while n!=0:
   num = num*10 + n%10
   n=int(n/10)
while num!=0:
    for i in range(num%10):
       print("hello"+str(i+1),end="")
    print("\n")
    num=int(num/10)