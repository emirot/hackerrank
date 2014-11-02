__author__ = 'nolanemirot'


def removeZeroReturnMin(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.pop(i)
            i -= 1
        i = i +  1
    if(len(arr)>0):
        return int(min(arr))
    return "false"


def cutStick(val):
    a = 0
    b = 0
    bol = True
    while bol:
        min = removeZeroReturnMin(val)
        if min == 0:
            return b
        if (min != "false"):
            i = 0
            b = 0
            while i < len(val):
                val[i] -= min
                i += 1
                b += 1
            print(b)
        else:
            bol = False
        a += 1


def main():
    n = int(input())
    i = 0
    val = []
    line = input().split()
   # print(line)
    while i < n:
         val.append(int(line[i]))
         i += 1
    cutStick(val)


if __name__ == '__main__':
   main()
