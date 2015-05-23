__author__ = 'nolanemirot'
import  re

def findHackerRank(give):
    if re.search("^hackerrank$",give,re.IGNORECASE):
        print("0")
    elif re.search("hackerrank$",give,re.IGNORECASE):
        print("2")
    elif re.search("^hackerrank",give,re.IGNORECASE):
        print("1")
    else:
        print("-1")


if __name__ == '__main__':
    nbTest = int(input())
    i = 0
    while i < nbTest:
        give = input()
        findHackerRank(give)
        i += 1