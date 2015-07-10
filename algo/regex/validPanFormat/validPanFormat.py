__author__ = 'nolanemirot'



import re
nb_case = int(input())
for i in range(nb_case):
    a = input()
    if (re.match('^[A-Z]{5}[0-9]{4}[A-Z]{1}',a)):
        print('YES')
    else:
        print('NO')