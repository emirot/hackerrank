from collections import Counter

def number_needed(a, b):
    cnt = Counter(a)
    cnt2 = Counter(b)
    a =  cnt2 - cnt
    b = cnt - cnt2 
    i = 0
    for e in a:
      i += a[e]

    for e in b:
      i += b[e]
    return i

a = input().strip()
b = input().strip()

print(number_needed(a, b))
