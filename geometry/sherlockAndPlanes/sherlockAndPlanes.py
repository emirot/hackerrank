__author__ = 'nolanemirot'


def checkIfInSamePlane(arr):
    y = 0
    x = 0
    while x < 3:
        same = True
        y = 0
        tmp = arr[y][x]
        while y < 4:
            if arr[y][x] != tmp:
                same = False
                break
            y +=1
        if same == True:
            return "YES"
        x += 1
    return "NO"



if __name__ == '__main__':
    nbTestCase =  int(input())
    indexCase = 0
    while indexCase < nbTestCase:
        i = 0
        arr = []
        while i < 4:
            line  = input()
            arr.append(list(map(int,line.split())))
            #print(arr)
            i+=1
        print(checkIfInSamePlane(arr))
        indexCase += 1



