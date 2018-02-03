#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 04                                                      |
===============================================================================
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import itertools

# generate list of candidate integers
vals2test = list(set([i*j for
                (i, j) in itertools.product(
                    range(100,1000), repeat=2)]))


def is_palindrome(n: int):
    """
    Determine whether or not n is a palindrome number.
    """
    test_result = True
    fwd = list(str(n))
    for i in range(len(fwd)):
        if not fwd[i]==fwd[-(i+1)]:
            test_result = False; break
    return(test_result)

all_palindromes = filter(is_palindrome, vals2test)
solution = max(all_palindromes)

# solution => 906609
