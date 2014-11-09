__author__ = 'nolanemirot'




def findArrayInArr(arr1,y1,x1,arr2,y2,x2):
    i = 0
    a = 0
    if(y2 > y1 or x2 > x1):
        return "NO"
    while i < y1:
        j = 0
        tmpy = i
        while j < x1:
            tmpx = j
            if(arr1[i][j] == arr2[0][0]):
                yy = tmpy
                xx1 = 0
                yy1 = 0
                a = 0
                if(tmpx + x2) < x1 and (tmpy + y2) < y1:
                    while yy1 < y1 and yy1 < y2 :
                        xx = tmpx
                        xx1 = 0
                        while xx1 < x1 and xx1 < x2:
                            if(arr2[yy1][xx1] == arr1[yy][xx]):
                               # print("same")
                                #print(arr2[yy1][xx1])
                                a += 1
                               # print("a",a)
                                if a == y2*x2:
                                    return "YES"
                            else:
                                break
                            xx += 1
                            xx1 += 1

                        #print("fisrt")
                        yy +=1
                        yy1+=1

            j += 1
        i += 1
   # print("a",a)
   # print("b",y2*x2)
    return "NO"


def getArray():
    arr1 = []
    j = 0

    line1 = input()
    y, x = line1.split()
    while j < int(y):
        currentLine = []
        line2 = input()
        ii = 0
        while ii < len(line2):
            currentLine.append(line2[ii])
            ii += 1
        arr1.append(list(map(int, currentLine)))
        j += 1
    return(arr1 , int(y), int(x))


if __name__ == '__main__':
    i = 0
   # arr1 = [[1,2,3],[5,6,8]]
   # arr2 = [[2,3],[6,8]]
  #  print(findArrayInArr(arr1,2,3, arr2,2,2))

    nbTestCase = int(input())
    while i < nbTestCase:
        arr1,y1,x1 = getArray()
        arr2,y2,x2 = getArray()
       # print(y1,x1)
        #print(y2,x2)
        #print(arr1)
        #print(arr2)
        print(findArrayInArr(arr1,y1,x1,arr2,y2,x2))
        i += 1

