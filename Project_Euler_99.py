#!/usr/bin/env python

"""
===============================================================================
Project Euler Problem 99                                                      |
===============================================================================
Comparing two numbers written in index form like 2^11 and 3^7 is not
difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""
import math
import csv

fpath = "./Datasets/p099_base_exp.txt"

with open(fpath, "r") as f:
    fcsv = csv.reader(f, delimiter=",", quoting=csv.QUOTE_NONE)
    results = [int(i[1]) * math.log(int(i[0])) for i in fcsv]

# add 1 to adjust for 0-based indexing
solution = results.index(max(results))+1

# solution => 709
