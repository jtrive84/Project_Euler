#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 10                                                      |
===============================================================================
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import itertools
import math


def is_prime(n):
    """Determine whether or not `n` is prime."""
    if n in (2, 3, 5, 7, 11, 13, 17, 19): return(True)
    if (n<=1 or n%2==0 or n%3==0): return(False)
    # determine upper limit of test range =>
    ulimit = (int(math.ceil(math.sqrt(n)))+1)
    return(not any(n%k==0 for k in range(3, ulimit, 2)))


def prime_generator():
    """
    Prime number generator. First prime generated will be 5
    (will not generate 2 & 3).
    """
    for i in itertools.count(start=1):
        for j in  ((6 * i) - 1, (6 * i) + 1):
            if is_prime(j): yield(j)


primes = [2, 3]
nbr = 2000000
pgen = prime_generator()

while primes[-1]<nbr: primes.append(next(pgen))
solution = sum(i for i in primes if i < nbr)

# solution => 142913828922
