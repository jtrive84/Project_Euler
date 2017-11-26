#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 22                                                      |
===============================================================================

Using p022_names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import string

fpath = "./Datasets/p022_names.txt"

# create letter-score mapping dict
ltrlkp = {i:j for (i,j) in
            zip(string.ascii_uppercase,
                range(1, len(string.ascii_uppercase)+1))}

with open(fpath, "r") as f:
    names = f.read().split(",")

names.sort()
scores = [sum(ltrlkp.get(i, 0) for i in n) for n in names]
solution = sum(i*j for (i, j) in zip(range(1, len(names)+1), scores))

# solution => 871198282
