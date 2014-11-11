__author__ = 'nolanemirot'


def insertionSort(arr):
    i = 1
    a = 0
    while i < len(arr):
        tmp = arr[i]
        j = i
        while (j > 0) and (tmp < arr[j-1]):
            arr[j] = arr[j-1]
            j -=1
            a += 1
        arr[j] = tmp
        i += 1
    print(a)
  #  print(arr)





if __name__ == '__main__':
    nbVals = int(input())
    line = input()
    arr2 = line.split()
    arr = list(map(int, arr2))
    insertionSort(arr)
    #insertionSort([2,1,3,1,2])