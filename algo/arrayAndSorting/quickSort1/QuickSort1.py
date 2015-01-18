__author__ = 'nolanemirot'

import sys

def quickSort(el, arr):
    left = []
    right = []
    i = 1
    while(i < len(arr)):
        if arr[i] < el:
            left.append(arr[i])
        else :
            right.append(arr[i])
        i+=1
    a = []
    a.append(el)
    return list(left+a+right)



if __name__ == '__main__':
    nbInA =  int(input())
    line = input()
    arr = list(map(int,line.split()))
    a = quickSort(arr[0], arr)
    for aa in a:
        print(aa,end=" ")