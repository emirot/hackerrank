__author__ = 'nolanemirot'


import sys



def insertionSort(tab):
    moves = 0
    for i in range( 1, len( tab ) ):
        j = i
        tmp = tab[i]
        while j > 0 and (tmp < tab[j-1]):
            tab[j] = tab[j-1]
            j -= 1
            moves += 1
            #printArar(tab)
        tab[j] = tmp
        i += 1
    #printArar(tab)
    return moves




def getInput():
    arr = []
    nb = int(input())
    line = input()
    arr = list(map(int,line.split()))
    return arr

if __name__ == '__main__':
    nbTest = int(input())
    i = 0
    while i < nbTest:
        arr = getInput()
        print(insertionSort(arr))
        i+= 1

