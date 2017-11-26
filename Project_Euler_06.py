#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem #6                                                      |
===============================================================================

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

# the sum of the squares of the first 100 natural numbers
sum_of_squares = sum(i**2 for i in range(1, 101))

# the square of the sum of the first 100 natural numbers
square_of_sum  = sum(j for j in range(1,101))**2

solution = square_of_sum - sum_of_squares

# solution => 25164150
