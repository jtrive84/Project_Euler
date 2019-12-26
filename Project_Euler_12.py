#!/usr/bin/env python
"""
===============================================================================
Project Euler Problem #12                                                     |
===============================================================================
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""
import itertools
import math


def isprime(n):
    """
    Determine whether or not `n` is prime.
    """
    if n in (2, 3, 5, 7, 11, 13, 17, 19):
        return(True)
    if (n<=1 or n%2==0 or n%3==0 or n%5==0):
        return(False)
    # determine upper limit of test range.
    ulim = (int(math.ceil(math.sqrt(n)))+1)
    return(not any(n%k==0 for k in range(3, ulim, 2)))



def get_factors(n):
    """
    Return factors of n, including 1 and n.
    """
    if isprime(n):
        res = [1, n]
    else:
        ulim = (n // 2) + 1
        if n%2==0:
            res = [i for i in range(1, ulim, 1) if n%i==0] + [n]
        else:
            res = [i for i in range(1, ulim, 2) if n%i==0] + [n]
    return(res)


trinum = 0
for i in itertools.count(start=1):
    trinum+=i
    numfact = len(get_factors(trinum))
    if numfact>500:
        break

solution = trinum
# solution => 76576500 (576)
