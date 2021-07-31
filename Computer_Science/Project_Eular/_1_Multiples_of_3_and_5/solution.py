#!/bin/python3

import sys

# variable to store the values of multiples of 3 or 5

# function for calculating sum
def sum_x(n):
    th = (n-1)//3
    fiv = (n-1)//5
    fif = (n-1)//15
    res = (3*(th*(th+1)//2)) + (5*(fiv*(fiv+1)//2)) - (15*(fif*(fif+1)//2))
    return res

t = int(input().strip())
res = []
for a0 in range(t):
    n = int(input().strip())
    print(sum_x(n))
