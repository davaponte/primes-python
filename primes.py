#!/usr/bin/env python
# -*- coding: utf-8 -*-

# A very, very simple program to find the prime numbers between 2 and 100
# David Aponte - October, 2018

import math

# Standard way:
def isPrimeNumber(Number):
    for k in range(2, int(math.sqrt(Number)) + 1):
        if (Number % k == 0):
            return False
    return True
   
for c in range(2, 101):
    if isPrimeNumber(c):
        print(c)



# Pythonic way:
primes = lambda Number : [k for k in range(2, Number) if not 0 in map(lambda c : k % c, range(2, int(math.sqrt(k)+1)))]
print(primes(100))

