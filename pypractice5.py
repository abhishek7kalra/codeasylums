# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:01:31 2019

@author: Abhishek
"""

n=int(input("number"))
n1=n
num=0
while n!=0:
   num = num*10 + n%10
   n=int(n/10)
if n1==num :
    print("pali")
else:
    print("not pali")