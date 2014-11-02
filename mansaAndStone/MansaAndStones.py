__author__ = 'nolanemirot'



testNb = []

def getTestCase():
    i = 0
    while i < 3:
        d = int(input())
        testNb.append(d)
        i = i + 1



def solve():
    nbStep = testNb[0]
    a = testNb[1]
    b = testNb[2]
    val = []
    resultat = []
    for x in range(nbStep):
        aa = (nbStep -x -1) * a
        bb = x * b
        val.append(aa + bb)
    for i in val:
        if i not in resultat:
            resultat.append(i)
    resultat.sort()
    for e in resultat:
        print(e , end=" ")
    print("")





def parse():
    d = int(input())
    i = 0
    while i < d :
        del testNb[:]
        getTestCase()
        solve()
        i = i + 1




def main():
    parse()


if __name__ == '__main__':
   main()

