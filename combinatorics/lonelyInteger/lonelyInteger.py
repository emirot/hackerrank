__author__ = 'nolanemirot'


def findLonelyInteger():
    nb = int(input())
    line = input()
    dic = {}
    arr = list(map(int,line.split()))
    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    #print(dic)
    for key,val in dic.items():
        if(val == 1):
            return key



if __name__ == '__main__':
    print(findLonelyInteger())