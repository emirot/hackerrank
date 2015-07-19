
import re

def isAlienUsername(line):
    if re.match('^[\.|_][0-9]{1,}[a-zA-Z]{0,}_?$', line):
        print("VALID")
    else:
        print("INVALID")



if __name__ == '__main__':
    nb_test_case = int(input())
    for i in range(nb_test_case):
        line  = input()
        isAlienUsername(line)