# -*- coding: utf-8 -*-
"""
NOTES FOR Python Class 1 of 5
Created on Mon Aug  4 10:06:50 2014

@author: nityakanuri
"""
#print all primes from 0 to 1000

#for n in range(1,1001):
#    for i in range(2,n):
#        if (n % i == 0):
#            break
#       else:
#           print n
# TO NOTE: This method did not work because, e.g., 999/2 does not equal,
#so immediately go to print. This is why it is bad to have print in loop
  

minIDx=1;
maxIDx=1001;
for i in range(minIDx,maxIDx):
    isPrime=True;
    for j in range(2,i):
        if (i % j == 0):
            isPrime=False;
            break
    if (isPrime ==True):
        print i