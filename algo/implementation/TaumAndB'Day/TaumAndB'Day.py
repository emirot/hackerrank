__author__ = 'nolanemirot'


def howMuckspendOnGift(B,W,X,Y,Z):

    casa =  B * X + W * Y
    casb =  X *(B + W)+ ( Z * W)
    casc = Y *(B+W) + (Z*B)
    #print(casa)
    #print(casb)
    #print(casc)
    return min([casa,casb,casc])


if __name__ == '__main__':
    nbTestCase = int(input())
    i = 0
    while i < nbTestCase:
        line =  input()
        arrl =  list(map(int,line.split()))
        B = arrl[0]
        W = arrl[1]
        line2 =  input()
        arrl2 =  list(map(int,line2.split()))
        X = arrl2[0]
        Y = arrl2[1]
        Z = arrl2[2]
        print(howMuckspendOnGift(B,W,X,Y,Z))
        i+=1