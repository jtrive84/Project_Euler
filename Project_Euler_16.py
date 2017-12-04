#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 16                                                      |
===============================================================================
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

# This is straightforward with arbitrary-precision arithmetic:
solution = sum(int(i) for i in list(str(2**1000)))

# solution => 1366
