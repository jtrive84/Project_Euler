#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 09                                                      |
===============================================================================
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import itertools

# substitute a^2 = (1000 - b - c)^2 into a^2 + b^2 = c^2
def eval_func(b, c):
    """
    Determine whether b, c force expression to 0.
    """
    return(((2 * b**2) - (2000 * b) - (2000 * c) + (2 * b * c) + 1000**2)==0)



for i in itertools.product(range(1, 1001), repeat=2):
    iter_b, iter_c = i[0], i[1]
    if eval_func(iter_b, iter_c):
        b, c = iter_b, iter_c; break

# determine a using b & c
a = 1000 - c - b

# triplet is (a, b, c): compute product
solution = a * b * c

# solution => 31875000
