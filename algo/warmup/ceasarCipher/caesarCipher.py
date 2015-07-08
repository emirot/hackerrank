__author__ = 'nolanemirot'



a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

A = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def caesar_cipher():
    e = input()
    line = input()
    k = int(input())
    res = ""
    for i in line:
        if i >= 'a' and i <= 'z':
            res += a[(a.index(i) + k) % 26]
        elif i >= 'A' and i <= 'Z':
            res += A[(A.index(i) + k) % 26]
        else:
            res += i
    print(res)



if __name__ == '__main__':
    caesar_cipher()
