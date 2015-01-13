__author__ = 'nolanemirot'



def swapIndexes(arr, index1, index2):
    #print("index1",index1)
    #print("index2",index2)
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp
    return arr


def findPlce(arr,el):
    i = 0
    while i < len(arr):
        if arr[i] < el:
            i += 1
        else:
            return i
    return i



def quickSortInPlace(arr, deb, fin):

    arr = arr[deb:fin]
    if len(arr) < 3:
        return arr

    greaterPassed = False
    pivot = arr[len(arr)-1]
    #print("pivot:", pivot)


    for i, a in enumerate(arr):
        if a > pivot:
            greaterPassed = True
        if a < pivot and greaterPassed == True:
            j = i
            while pivot < arr[j-1]:
                j -= 1
            arr = swapIndexes(arr,i,j)
    newPlace = findPlce(arr, pivot)
    print("newPlace",newPlace)
    arr = swapIndexes(arr, len(arr)-1, newPlace)

    l = quickSortInPlace(arr,0,newPlace)
    r = quickSortInPlace(arr,newPlace,len(arr))
    print("l",l+r)
    return l + r


if __name__ == '__main__':
    nbNum =  int(input())
    line = input()
    arr = list(map(int,line.split()))
    arr = quickSortInPlace(arr,0,len(arr))
    print(arr)
