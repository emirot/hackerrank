

import re
nb_case = int(input())
for i in range(nb_case):
    a = input()
    if (re.match('^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}',a)):
        print('VALID')
    else:
        print('INVALID')