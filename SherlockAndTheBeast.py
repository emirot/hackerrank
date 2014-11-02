__author__ = 'nolanemirot'

nbTestCase = int(input())


def findNbDigit(N):
    i = 0
    a = N
    rep = ""
    five = 0
    while a > 0:
        if a % 3 == 0:
            five = a
            break
        a -= 5
    trees = N - five
    if five <= 0 and trees % 5 != 0:
        return print("-1")
    while(five > 0):
        rep += "5"
        five -= 1
    while trees > 0:
        rep += "3"
        trees -= 1
    print(rep)



while nbTestCase > 0:
    N = int(input())
    findNbDigit(N)
    nbTestCase = nbTestCase - 1