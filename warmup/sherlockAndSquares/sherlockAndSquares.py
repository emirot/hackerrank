__author__ = 'nolanemirot'

import math


def findNbSquaresInRange(a, b):
    i = 0
    res = 0
    res = math.floor(math.sqrt(b)) - math.floor(math.sqrt(a))
    print(res)



if __name__ == '__main__':
    nbTestCase = int(input())
    i =0
    arr = []

    while i < nbTestCase:
        line = input()
        arr = line.split(' ')
        if(len(arr)==2):
            findNbSquaresInRange(int(arr[0]),int(arr[1]))
        i += 1
