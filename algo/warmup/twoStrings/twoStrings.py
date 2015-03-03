__author__ = 'nolanemirot'



def findTwoStrings(s1, s2):
    dic = []
    for n in s1:
        if n not in dic:
            dic.append(n)
    for s in s2:
        if s in dic:
            return "YES"
    return "NO"



if __name__ == '__main__':
    nbTestCase = int(input())
    for i in range(0, nbTestCase):
        s1 = input()
        s2 = input()
        print(findTwoStrings(s1, s2))