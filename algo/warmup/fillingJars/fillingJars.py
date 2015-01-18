





line = input().split()
nbjars = int(line[0])
mLines = int(line[1])



i = 0
total = 0

while i < mLines:
    linep = input().split()
    a = int(linep[0])
    b = int(linep[1])
    k = int(linep[2])
    total += ((b+1 -a) * k)
    i = i + 1

print(int(total/nbjars))