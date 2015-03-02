__author__ = 'nolanemirot'

import  re

def validPhoneNumber(give):
    if re.search("^(7|8|9)([0-9]{9})$", give):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    nbTest = int(input())
    i = 0
    while i < nbTest:
        give = input()
        validPhoneNumber(give)
        i += 1