#!/bin/python3

import math
import os
import random
import re
import sys




# Complete the hourglassSum function below.
def hourglassSum(arr):

    # check arr
    col_len = len(arr[0]) - 1
    max_ = float('-inf')

    for row in range(0, len(arr)):
        for col in range(0, len(arr[0])):
            if col + 2 <= col_len and row + 2 <= len(arr) -1:
                max_ = max(max_, sum([arr[row][col], arr[row][col+1], arr[row][col+2], arr[row+1][col+1], arr[row+2][col], arr[row+2][col+1], arr[row+2][col+2]]))
    return max_
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
