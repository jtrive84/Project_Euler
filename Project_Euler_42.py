#!/usr/bin/env python

"""
===============================================================================
Project Euler #42                                                             |
===============================================================================
The nth term of the sequence of triangle numbers is given by tn = (1/2)n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value
is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle
words?
"""
import string
import itertools

fpath = "./Datasets/p042_words.txt"

# create letter-score mapping dict
ltrlkp = {i:j for (i,j) in
            zip(string.ascii_uppercase,
                range(1, len(string.ascii_uppercase)+1))}


def word2score(word, lkp):
    """
    Determine the numeric score fgor word using ltrlkp.
    """
    return(sum(lkp.get(i, 0) for i in tuple(word.upper().strip())))


def tri_func(n):
    """
    Return evaluated triangle function.
    """
    return(int(.5 * n * (n + 1)))


def get_tris(upto):
    """
    Return list of triangle numbers from 1 to upto inclusive.
    """
    trilst = list()
    for i in itertools.count(start=1):
        iter_tri = tri_func(i)
        if iter_tri<=upto:
            trilst.append(iter_tri)
        else:
            break
    return(trilst)


with open(fpath, 'r') as f:
    words = f.read().split(",")
    words = [i.replace('\"', "") for i in words]


# determine max word score and triangle numbers list
max_score = max(word2score(i, ltrlkp) for i in words)
all_tris = get_tris(max_score)

triangle_words = sum(1 if i in
                      all_tris else 0 for i in
                         [word2score(j,ltrlkp) for j in words])

# solution => 162
