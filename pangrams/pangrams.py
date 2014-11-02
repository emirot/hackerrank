__author__ = 'nolanemirot'



alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

l = []

def isInArray(letter):
    i = 0
    while(i < len(l)):
        if l[i][0] == letter:
            l[i][1] += 1
            return True
        i += 1
    return False


def stringIsPangram():
    i = 0
    a  =0
    while(i < len(l)):
        j = 0
        while(j < len(alpha)):
            if l[i][0] == alpha[j]:
                a += 1
            j += 1
        i += 1
    if(a == len(alpha)):
        return True
    return False

def pangrams():
    inputString = input()
    i = 0
    inputString = inputString.lower()
    while i < len(inputString):
        if isInArray(inputString[i]) == False:
            if inputString[i] != ' ':
                l.append([inputString[i], 1])
        i += 1
    if stringIsPangram():
        print("pangram")
    else:
        print("not pangram")
    #print(l)


if __name__ == '__main__':
    pangrams()