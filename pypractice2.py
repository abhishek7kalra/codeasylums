# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:30:55 2019

@author: Abhishek
"""

def sieve(n1,n):
    prime  = [True for i in range(n+1)]
    p=2
    while(p*p <= n):
        if(prime[p] == True):
            for i in range(p*p, n+1, p):
                prime[p] = False
        p=p+1
    for p in range(n1,n):
        if prime[p]== True:
            print(p)
n1=int(input("lower limit"))
n=int(input("upper limit"))
sieve(n1,n)