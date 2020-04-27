#!/bin/python3

import math
import os
import random
import re
import sys


def ceasar_cipher(n, s, k):
    new_str = ""
    n = k
    if n > 25:
        n = n % 26
    for e in s:
        tmp_n = n
        if ord(e) >= ord('a') and ord(e) <= ord('z'):
            if (ord(e) + n) <= ord('z'):
                new_str += chr(ord(e) + n)
            elif (ord(e) + n) > ord('z'):
                tmp_n -= abs(ord('z') - ord(e))
                new_str += chr(ord('a') + tmp_n - 1)
        elif ord(e) >= ord('A') and ord(e) <= ord('Z'):
            if ord(e) + n <= ord('Z'):
                new_str += chr(ord(e) + n)
            elif (ord(e) + n) >= ord('Z'):
                tmp_n -= ord('Z') - ord(e)
                new_str += chr(ord('A') + tmp_n - 1)
        else:
            new_str += e
    return new_str


if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())
    print(ceasar_cipher(n,s,k))
