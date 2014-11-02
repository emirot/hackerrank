__author__ = 'nolanemirot'
import sys



def insertionSort(tab):

    for i in range( 1, len( tab ) ):
        j = i
        tmp = tab[i]
        while j > 0 and (tmp < tab[j-1]):
            tab[j] = tab[j-1]
            j -= 1
        tab[j] = tmp
        printArar(tab)
        i += 1
    return tab

def printArar(arr):
    i = 0
    while i < len(arr):
        sys.stdout.write(arr[i]+" ")
        i += 1
    sys.stdout.write("\n")


def getInput():
    arr = []
    nb = int(input())
    line = input()
    arr = line.split(' ')
    return arr

if __name__ == '__main__':
    arr = getInput()
    insertionSort(arr)
