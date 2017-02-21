#!/bin/python3

import sys
from collections import Counter

def lonely_integer(a):
    if len(a) == 1:
        return a[0]
    c = Counter(a)

    for e in c:
        if c[e] == 1:
            return e

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
