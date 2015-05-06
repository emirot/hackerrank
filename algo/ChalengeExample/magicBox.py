

# Enter your code here. Read output from STDIN. Print input to STDOUT


def parseArray(row, column):
    i = 0
    arr = []
    #print(column)
    while i < row:
        lineToParse = input()
        #print(lineToParse)
        #print(lineToParse[0])
        j = 0
        tmp=[]
        while j < column:
            tmp.append(lineToParse[j])
            j = j + 1
        arr.append(tmp)
        i = i + 1
    return arr


def checkIfEqualsPerLine(arr):
    i =0
    a = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            a += 1
        i = i + 1
    if a == len(arr)-1:
        return True
    return False



def checkAllLine(arr):
    i = 0
    sameOnLine = 0
    while i < len(arr):
        if checkIfEqualsPerLine(arr[i]):
            sameOnLine = sameOnLine + 1
        i = i + 1
    return sameOnLine


def shiftColumn(arr,row, column, nbColumnToShif):
    y = 0
    while y < column:
        x = 0
        if y == nbColumnToShif:
            while x < row:
                #print(arr[x][y])
                if arr[x][y] == 'T':
                    arr[x][y] = 'P'
                elif arr[x][y]=='P':
                    arr[x][y] ='T'
                x = x + 1
        y = y + 1
    return arr

def findMaxWichies(arr1, row, column):
    max = checkAllLine(arr1)
    print("max",max)
    i = 0
    while i < column:
        arr = shiftColumn(arr1,row, column,i)
        print(arr)
        tmp = checkAllLine(arr)
        if tmp > max:
            max = tmp
        print("MAX",max)
        i = i + 1
    return max

if __name__ == '__main__':
    firstLine  = input()
    rowAndColumn = list(map(int, firstLine.split()))
    row =  rowAndColumn[0]
    column = rowAndColumn[1]
    arr = parseArray(row, column)
    #checkAllLine(arr)
    #shiftColumn(arr,row,column,1)
    print(findMaxWichies(arr,row,column))
    #print(checkIfEqualsPerLine(['P','T','P']))