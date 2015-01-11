__author__ = 'nolanemirot'




def cutAnagramics(str):
    i = 0
    j = 0
    arr = []
    while i < len(str):
        j = i
        j+=1
        while j < len(str):
            #print(j)
            #print(str[i:j])
            arr.append(str[i:j])
            j+=1
        #print(str[i:j+1])
        arr.append(str[i:j])
        i+=1
    return arr


def returnNbFindInArray(key, arr):
    c = 0
    for i in arr:
        if key == i:
            c += 1
    return c



def findAnagramics(arr):
    #print(arr)
    arra = []
    dic = {}
    count = 0
    count = 0
    for a in arr:
        arra.append(''.join(sorted(a)))
    print(arra)
    for b in arra:
        dic[b] = 0
    print(dic)
    for c in arra:
        if c in dic:
            dic[c] += 1
    print(dic)
    for d in dic:
        if dic[d] == 2:
            count += 1
        elif dic[d] > 2:
            count += dic[d]
    #print(count)
    return count


if __name__ == '__main__':
    nbTestCase = int(input())
    i = 0
    while i < nbTestCase:
        line = input()
        arr = cutAnagramics(line)
        nb = findAnagramics(arr)
        print(nb)
        i += 1
