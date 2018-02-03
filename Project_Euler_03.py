#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 03                                                      |
===============================================================================
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import itertools
import math



def is_prime(n: int):
    """
    Determine whether or not `n` is prime.
    """
    if n in (2, 3, 5, 7, 11, 13, 17, 19, 23):  return(True)
    elif (n<=1 or n%2==0 or n%3==0 or n%5==0): return(False)
    # determine upper limit of test range =>
    ulimit = (int(math.ceil(math.sqrt(n)))+1)
    return(not any(n%k==0 for k in range(3, ulimit, 2)))


# All primes are of the form 6k+/-1 with the exception of 2 & 3
# https://en.wikipedia.org/wiki/Primality_test#Simple_methods
def prime_generator():
    """
    Prime number generator. First prime generated will be 5
    (will not generate 2 & 3).
    """
    for i in itertools.count(start=1):
        for j in  ((6 * i) - 1, (6 * i) + 1):
            if is_prime(j):
                yield(j)



nbr    = 600851475143
primes = [2, 3]
pgen   = prime_generator()

while primes[-1] < math.ceil(math.sqrt(nbr)):
    primes.append(next(pgen))

solution = max(i for i in enumerate(primes) if nbr%i[1]==0)[1]

# solution => 6857
