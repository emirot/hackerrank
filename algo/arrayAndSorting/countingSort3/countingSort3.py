__author__ = 'nolanemirot'


__author__ = 'nolanemirot'


__author__ = 'nolan'



def printNTime(val, n):
    i =0
    while i < n:
        print(val,end=" ")
        i +=1



if __name__ == '__main__':
    nbVal = int(input())
    i = 0
    arr = []
    while i < nbVal:
        l = input()
        tmp = list(l.split())
        arr.append(int(tmp[0]))
        i += 1
    dic = {}
    for i in range(0, 100):
        dic[i] = 0
    a = 0
    for val in arr:
        if val in dic:
            dic[val] += 1
        else:
            dic[val] = 0
    v = 0
    for i in range(0,100):
        if i in dic:
            v+=dic[i]
            print(v,end=" ")

