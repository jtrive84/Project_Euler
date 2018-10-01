#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 29                                                      |
===============================================================================
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""
import itertools

for i in itertools.count(start=1):
    v1, v2 = i, 2 * i
    s1, s2 = set(str(v1)), set(str(v2))
    if len(s1.difference(s2))==0:
        vmults = [v1 * j for j in range(1, 7)]
        dsets  = [set(str(j)) for j in vmults]
        if all(j==dsets[0] for j in dsets):
            print(vmults)
            break

# solution => 142857 [142857, 285714, 428571, 571428, 714285, 857142]
