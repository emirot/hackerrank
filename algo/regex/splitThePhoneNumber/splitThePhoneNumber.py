

import re

nb_case = int(input())
for i in range(nb_case):
    s = input()
    res = re.split('-|\s', s)
    a = "CountryCode={},LocalAreaCode={},Number={}".format(res[0],res[1],res[2])
    print(a)