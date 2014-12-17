__author__ = 'nolanemirot'



def printArr(arr):
    for a in arr:
        print(a, end=" ")
    print()

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    left = []
    right = []
    within = []
    pivot = arr[0]
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el > pivot:
            right.append(el)
        else:
            within.append(el)


    left = quickSort(left)
    within = quickSort(within)
    right = quickSort(right)
    printArr(left + within + right)
    return left + within + right


if __name__ == '__main__':
    nbVal =  int(input())
    line = input()
    arr = list(map(int, line.split()))
    quickSort(arr)