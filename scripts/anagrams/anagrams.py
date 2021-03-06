#! /usr/bin/env python3
# Time-stamp: <2019-04-07 18:17:32 christophe@pallier.org>
# License: GPL-2

"""Input: a text file with one word per line
   Output: all anagrams"""

import sys

# read in the lines from the file given as argument
dictionary = open(sys.argv[1]).read().splitlines()

# 'ana' will contain lists of anagrams, indexed by their letters
ana = {}

for w in dictionary:
    # the key is the sorted letters from w
    l = list(w)
    l.sort()
    key = "".join(l)

    # insert w in the list key
    if key in ana:
        ana[key].append( w )
    else:
        ana[key] = [ w ]

# print the anagrams
for k in ana:
    if len(ana[k]) > 1:
        for w in ana[k]:
            print(w, end=" ")
        print(end="\n")



