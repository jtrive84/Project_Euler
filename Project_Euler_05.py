#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 05                                                      |
===============================================================================
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
import itertools

# Test even integers above 2520: 2540, 2560, 2580... and check whether
# number is evenly divisible by 11-19, since division by 11-19 implies
# division by 1-10.

def div_test(n: int):
    """
    Determine whether n is divisible by 1-19.
    """
    return(all(n%i==0 for i in range(11,20)))


for i in itertools.count(start=2540, step=20):
    if div_test(i):
        solution = i; break

# solution => 232792560
