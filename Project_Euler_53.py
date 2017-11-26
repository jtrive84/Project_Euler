#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 53                                                      |
===============================================================================
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

        nCr = n!/r!(n−r)!,

where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are
greater than one-million?
"""

def factorial(n):
    """
    Return facorial of n.
    """
    if n<=1: return(1)
    else:
        return(n * factorial(n - 1))


def binomial_coeff(n, k):
    """
    Return the result of `n choose k`.
    """
    return(factorial(n)/(factorial(k) * factorial(n - k)))


def combin_test(n, threshold):
    """
    Determine the number of values exceeding threshold
    from calculated binomial coefficient.
    """
    return(sum(1 if j>threshold else 0
            for j in [binomial_coeff(n, i)
                for i in range(2, n)]))



solution = sum(combin_test(i, 1000000) for i in range(1, 101))

# solution => 4075
