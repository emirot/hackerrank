__author__ = 'nolanemirot'

a = "abcde"
b = "bc"

if b in a:
    print("tru")
else:
    print("false")

for n in range(2, 19):
    for x in range(2, n):
        print("n%x",n,x,n%x)
        if n % x == 0:
             print(n, 'equals', x, '*', n/x)
             break
    else:
        print(n, 'is a prime number')