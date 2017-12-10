#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 20                                                      |
===============================================================================
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(n):
    """
    Return factorial of n.
    """
    if n<=1:
        return(1)
    else:
        return(n*factorial(n-1))


# convert result to a list of ints, the sum
solution = sum(int(i) for i in list(str(factorial(100))))

# solution => 648
