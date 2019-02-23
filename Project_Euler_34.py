#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 34                                                      |
===============================================================================
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of 
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
import itertools
import numpy as np
from scipy.special import factorial


keepers = []
for i in itertools.count(start=3):
    intarr = np.asarray([int(j) for j in list(str(i))])
    fctsum = factorial(intarr).sum()
    if i==fctsum:
        keepers.append(i)
    if i==1000000:
        break

print(keepers) # solution => 40730

