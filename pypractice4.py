# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:54:34 2019

@author: Abhishek
"""

n1=int(input("number1"))
if(n1%6==0):
    print("window")
elif(n1%6==1):
    print("window")
elif(n1%6==2):
    print("middle")
elif(n1%6==5):
    print("middle")
elif(n1%6==3):
    print("aisle")
elif(n1%6==4):
    print("aisle")
print(n1+6)
