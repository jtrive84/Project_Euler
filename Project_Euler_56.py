#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 56                                                      |
===============================================================================
A googol (10100) is a massive number: one followed by one-hundred zeros;
100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the
maximum digital sum?
"""
maxsum = (0, 0)

for i in range(1,100):
    lvals = [i**j for j in range(1,100)]
    lvals = [list(str(j)) for j in lvals]
    lvals = [[int(j) for j in k] for k in lvals]
    imax  = max(sum(j) for j in lvals)
    maxsum = (i, imax) if imax > maxsum[1] else maxsum

# solution => (99, 972)
