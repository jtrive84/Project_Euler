#!/usr/bin/env python
"""
===============================================================================
Project Euler Problem 27                                                      |
===============================================================================
Euler discovered the remarkable quadratic formula:

                    n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0 ≤ n ≤ 39. However, when n=40, 40^2 + 40 + 41 = 40(40+1)+41 is
divisible by 41, and certainly when n=41,41^22+41+41 is clearly divisible by
41.

The incredible formula:

                    n^2 − 79n + 1601

was discovered, which produces 80 primes for the consecutive values
0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.


Considering quadratics of the form:

                    n^2 + a*n + b, where |a| < 1000 and |b| ≤ 1000

where |n| is the modulus/absolute value of n e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""
import itertools
import math


def isprime(n):
    """
    Determine whether or not `n` is prime.
    """
    prime_ind = False
    init_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
        67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137,
        139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
        ]

    if n in init_primes:
        prime_ind = True

    elif (n<=1 or n%2==0 or n%3==0 or n%5==0):
        prime_ind = False

    else:
        # Determine upper limit of test range.
        ulimit    = (int(math.ceil(math.sqrt(n)))+1)
        prime_ind = not any(n%k==0 for k in range(3, ulimit, 2))
    return(prime_ind)



def primeseq(*coeffs):
    """
    Determine the longest sequence of prime numbers starting at 0.
    `func` is assumed to take a single integer argument, and returns
    the result of the primality test.
    """
    a, b = coeffs
    primes = list()

    def poly(n):
        """
        Primality test for polynomial n^2 + a*n + b.
        """
        v = n**2 + a * n + b
        return((v, isprime(v)))

    for i in itertools.count(start=0):
        iterval = poly(i)
        if iterval[1]:
            primes.append(iterval[0])
        else:
            break

    return(primes)



# Generate iterable containing polynomial coefficients.
longest = {'a':None, 'b':None, 'length':-1, 'prod':-1}

for v in itertools.product(range(-999, 1000), repeat=2):
    iterseq = primeseq(*v)
    iterlen = len(iterseq)
    if iterlen > longest["length"]:
        a, b = v
        longest["a"]      = a
        longest["b"]      = b
        longest["length"] = iterlen
        longest["prod"]   = a * b

# solution => -59231
