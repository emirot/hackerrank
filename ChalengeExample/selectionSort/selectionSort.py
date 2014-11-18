__author__ = 'nolanemirot'



def selectionSort(arr):
    i = 0

    while i < len(arr):
        toSwap = -1;
        tmp = arr[i]
        j = i + 1
        while j < len(arr) -1:
            if tmp > arr[j]:
                tmp = arr[j]
                toSwap = j
            j += 1
        if(toSwap >= 0):
            tmp2 = arr[toSwap]
            arr[toSwap] = arr[i]
            arr[i] = tmp2
        i+=1
    print(arr)






if __name__ == '__main__':
    selectionSort([4,3,5,1,23,52,4,9])