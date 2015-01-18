__author__ = 'nolanemirot'


def recurCalc(nb):
    res = 0
    while(nb!=0):
        res += nb -1
        nb-=1
    return res


def calcHandShake(nb):
    if nb == 1:
        return 0
    elif nb == 2:
        return 1
    else:
        return recurCalc(nb)





if __name__ == '__main__':
    nbCases =  int(input())
    i = 0
    while i < nbCases:
        nb = int(input())
        print(calcHandShake(nb))
        i += 1
