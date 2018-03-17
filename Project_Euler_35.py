#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 35                                                      |
===============================================================================
The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import itertools
import math



def isprime(n:int):
    """
    Determine whether or not `n` is prime.
    """
    if n in (2, 3, 5, 7, 11, 13, 17, 19): return(True)
    if (n<=1 or n%2==0 or n%3==0): return(False)
    # determine upper limit of test range =>
    ulimit = (int(math.ceil(math.sqrt(n)))+1)
    return(not any(n%k==0 for k in range(3, ulimit, 2)))


def primes_upto(n:int):
    """
    Return all primes numbers from 2 up to n.
    """
    # Initialize stream of primes.
    plist   = [2, 3]
    pstream = prime_stream()
    iterp   = 3
    while iterp<n:
        iterp = next(pstream)
        plist.append(iterp)
    return(plist)



def rotator(n:int):
    """
    Return all rotations of n as list.
    """
    rotations = set([n])
    strn      = str(n)
    strnlst   = list(strn)

    for i in range(len(strnlst)-1):
        init = strnlst.pop(0)
        strnlst.append(init)
        iterint = int("".join(strnlst))
        rotations.add(iterint)

    return(list(rotations))



# Generate list of primes from 2-1,000,000.
primes = primes_upto(1000000)
circulars  = set()


for i in primes:
    iterp = rotator(i)
    if all(isprime(j) for j in rotator(i)):
        circulars.add(i)

# solution => len(circulars) = 55

















