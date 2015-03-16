__author__ = 'nolanemirot'
from operator import itemgetter



if __name__ == '__main__':
    nbCase =  int(input())
    arr = []
    for i in range(0, nbCase):
        line = input()
        val = float(input())
        l = list([line, val])
        arr.append(l)

    arr.sort(key=itemgetter(1))
    min= arr[0][1]
    for el in arr:
        if el[1] != min and el[1] > min:
            val = el[1]
            break
    last = []
    for el in arr:
        if el[1] == val:
            last.append(el)
    last.sort(key=itemgetter(0))
    for el in last:
       print(el[0])