__author__ = 'nolanemirot'



def insertionSort(arr):

    i=1
    while i < len(arr):
        tmp = arr[i]
        j = i
        while(j > 0 and tmp < arr[j-1]):
            arr[j] = arr[j-1]
            j-=1
        arr[j] = tmp
        i+=1
    return arr




if __name__ == '__main__':
   a = insertionSort([4,3,42,52,1,2,4])
   print(a)