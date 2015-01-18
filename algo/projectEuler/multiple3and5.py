

def findNbTerm(val, mul):
    val -= 1
    a = mul
    b = 1 * mul
    val = val + b
    res = int(val / a)
    return res

def cal(nbTerme, mult):
    der = mult * (nbTerme - 1)
    #print("der", der)
    res = (nbTerme) * (int(der) / 2)
    #$print("resC", res)
    return int(res)


def oldCal(val, mult):
    i = 0
    sum = 0
    while i < val:
        if i % mult == 0:
            sum = sum + i
        i = i + 1
    return sum


def ocal(val):
    i = 0
    sum = 0
    while i < val:
        if i % 15 == 0:
            sum = sum + i
        i = i + 1
    return sum

def parse():
    nbCase = int(input())
    i = 0
    while i < nbCase:
        val = int(input())
        res3 = findNbTerm(val, 3)
        res5 = findNbTerm(val, 5)
        res7 = findNbTerm(val, 15)
        r3 = cal(res3, 3)
        r5 = cal(res5, 5)
        r15 = cal(res7, 15)
        print(r3 + r5 - r15)
        i = i + 1






parse()



"""
r1 = oldCal(10, 3)
r2 = oldCal(10, 5)
r3 = r1 + r2
print(r3)


r1 = oldCal(100, 3)
r2 = oldCal(100, 5)
r3 = r1 + r2
print(r3)
"""