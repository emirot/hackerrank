__author__ = 'nolanemirot'


def closestToZero(arr, nb):

    a = True
    print(arr)
    while a:
        i = 0
        a = False
        while i < len(arr) - 1:
            if arr[i][0] > arr[i+1][0]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                a = True
            ## Should be tested but not !!!!!!!!!!
            # if arr[i][0] == arr[i+1][0] and  arr[i][1] > arr[i+1][1]:
            #     tmp = arr[i]
            #     arr[i] = arr[i+1]
            #     arr[i+1] = tmp
            #     a = True
            i += 1
    for el in arr:
        print(el[2],end=" ")




def jimAndOrder(array):
    tmp = []
    i = 1
    for el in array:
        tmp.append([el[0]+el[1],el[0],i])
        i += 1
    #print(tmp)
    t = tmp[0][0]
    i = 0
    a = 0
    b = 0
    # print("tmpi[0]",tmp)
    j = 0
    #closestToZero(tmp,len(tmp))
    tmp.sort(key = lambda x:x[0])
    print(tmp)
    print(' '.join([str(x[2]) for x in tmp]))





if __name__ == '__main__':
    nbCase = int(input())
    array = []
    for i in range(nbCase):
        line = input()
        arr = list(map(int,line.split()))
        array.append(arr)
    #print(array)

    jimAndOrder(array)