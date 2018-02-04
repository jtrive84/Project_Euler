#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 25                                                      |
===============================================================================
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

    F1  = 1
    F2  = 1
    F3  = 2
    F4  = 3
    F5  = 5
    F6  = 8
    F7  = 13
    F8  = 21
    F9  = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""
import itertools


def fib_stream():
    """
    Return the Fibonacci sequence as a generator with
    corresponding index.
    """
    prev, curr, trkr = 1, 1, 2
    for i in itertools.count(start=3):
        iterf = (curr+prev)
        prev, curr  = curr, iterf
        yield((i,iterf))


# Initialize fibonacci stream.
fstream = fib_stream()

while True:
    iterf   = next(fstream)
    iteridx = iterf[0]
    iterfib = iterf[1]
    iterlen = len(str(iterfib))
    if iterlen>=1000: break

# solution => 4782
