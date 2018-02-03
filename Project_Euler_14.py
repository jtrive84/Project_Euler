#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem #14                                                     |
===============================================================================

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
import multiprocessing


def collatz_test(n):
    """
    If n is even, return (n/2), else return (3n+1).
    """
    return((n/2) if n%2==0 else (3*n+1))


def chain_length(n):
    """
    Return the number of collatz iterations required to
    arrive at 1.
    """
    if n<=0: return(None)
    cntr, tstint = 0, n
    while tstint!=1:
        cntr+=1
        tstint = collatz_test(tstint)
    return(n, cntr)



if __name__ == "__main__":

    # initialize parallel processing pool
    # From docs (https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing):
    #
    #   For very long iterables using a large value for chunksize can make the
    #   job complete much faster than using the default value of 1.
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    pool_outputs = pool.imap(chain_length, range(1, 1000000), chunksize=1000)
    pool.close()
    pool.join()

    solution = max((i for i in pool_outputs), key=lambda x: x[1])

    # solution => (837799, 524)
