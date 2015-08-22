__author__ = 'nolanemirot'



stre = input()

s = ""

for i in stre:
    asci = ord(i)
    if asci >= 97 and asci <= 122:
        s += i.upper()
    elif asci >=65 and asci <= 90:
        s += i.lower()
    else:
        s += i
print(s)