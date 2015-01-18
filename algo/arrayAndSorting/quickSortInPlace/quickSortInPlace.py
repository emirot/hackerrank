__author__ = 'nolanemirot'



def swapIndexes(arr, index1, index2):
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



if __name__ == '__main__':
    nbNum =  int(input())
    line = input()
    arr = list(map(int,line.split()))
    arr ,n= quickSortInPlace(arr,0,len(arr))
    print("Last",arr)
    arr = quickSortInPlace(arr,0,n)
    print(arr)
    #pivot -= 1
    #print("pivot",pivot)
    #quickSortInPlace(arr,0,pivot)

#1 4 3 2 32 34 5 46 576 87 54 21 43