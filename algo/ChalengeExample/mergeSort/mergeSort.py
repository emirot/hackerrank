__author__ = 'nolanemirot'


def merge(leftA, rightB):
    result = []
    ia = 0
    ib = 0
    while ia < len(leftA) and ib < len(rightB):
        if leftA[ia] <= rightB[ib] :
            result.append(leftA[ia])
            ia+=1
        else:
            result.append(rightB[ib])
            ib+=1
    if leftA:
        result.extend(leftA[ia:])
    if rightB:
        result.extend(rightB[ib:])
    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    middle = int(len(arr) / 2)
    left = arr[:middle]
    right = arr[middle:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left,right)


if __name__ == '__main__':
    print(mergeSort([4,3,2,4,5,6,7,9,78,54,23,43]))