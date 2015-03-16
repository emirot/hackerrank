__author__ = 'nolanemirot'
import re



nbCase  = int(input())

for nbCase in range(0, nbCase):
    a = input()
    if re.search("^hi\s[^d]",a,re.IGNORECASE):
        print(a)


