__author__ = 'nolanemirot'




def calcEqualCase(flow):
    i =0
    res = 0
    while i < len(flow):
        res += flow[i]
        i+=1
    return res



def findLowerInDic(dic):
    min = min(dic.intervalues)

def flowers():
    n, k = input().split()
    k = int(k)
    us = []
    i = 0
    while i < k:
        us.append(0)
        i+=1
    #print(us)
    line = input()
    flow = list(map(int, line.split()))
    res = 0
    if k == len(flow):
        #print("len == k")
        return calcEqualCase(flow)
    elif len(flow) > k :
        #print("in else")
        user = 0
        while (len(flow)!=0):
            maxF  = max(flow)
            i = 0
            ret = min(us)
            #print("ret", ret)
            index = us.index(ret)
            us[index] += 1
            res += (1 + ret) * maxF
            #print(maxF)
            flow.remove(maxF)
        return res
    else:
        print("ERROR")





if __name__ == '__main__':
    print(flowers())