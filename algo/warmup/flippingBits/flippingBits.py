__author__ = 'nolanemirot'




#a  = 0b1

#print(int('11111111111111111111111111111110',2))

#a = bin(1)
#print(a)

#print(a^a)

def addBits(nb):
    num = bin(nb)
    num = num[2:]
    s = str(nb)
    slen = len(num)
    a = 32 - slen
    string = ''
    while a > 0:
        string += '0'
        a-=1
    return string + num


def flipBits(nb):
    i = 0
    neww = ''
    while i < len(nb):
        if (nb[i]=='0'):
            neww += "1"
        else:
            neww += '0'
        i += 1
    val = int(neww,2)
    return val


if __name__ == '__main__':
    a = int(input())
    i = 0
    while i < a:
        nb = int(input())
        chi = addBits(nb)
        print(flipBits(chi))
        i+=1