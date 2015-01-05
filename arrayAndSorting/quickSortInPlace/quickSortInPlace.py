__author__ = 'nolanemirot'



def swapIndexes(arr, index1, index2):
    print("index1",index1)
    print("index2",index2)
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp
    return arr



def quickSortInPlace(arr):
    greaterPassed = False
    greaterPosition = 0
    pivot = arr[len(arr)-1]
    print("pivot:",pivot)

    for i, a in enumerate(arr):
        if a > pivot:
            greaterPassed = True
            print(greaterPassed)
            greaterPosition = i
        if a < pivot and greaterPassed == True:
            j = i
            print("LALAL")
            print("J", j)
            while pivot < arr[j-1] :
                j -= 1
            print("JJ",j)
            arr = swapIndexes(arr,i,j)
    print(arr)


if __name__ == '__main__':
    nbNum =  int(input())
    line = input()
    arr = list(map(int,line.split()))
    quickSortInPlace(arr)