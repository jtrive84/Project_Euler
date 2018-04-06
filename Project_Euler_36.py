#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 36                                                      |
===============================================================================
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

def revlist(l):
    """
    Return l with items in reverse order.
    """
    reslist = list()
    llen = len(l)
    for i in range(llen):
        reslist.append(l[llen-i-1])
    return(reslist)


def ispalindrome(l)    :
    """
    Return True if sequence if symmetric.
    """
    backward = revlist(l)
    return(all(i==j for i,j in zip(l,backward)))


keepers = list()

for i in range(1,1000000):

    base10 = list(str(i))
    base2  = str(bin(i)).replace("0b","")

    if ispalindrome(base10):

        if ispalindrome(base2):

            keepers.append(i)

# solution => 872187
