import numpy

inp = input()
row, col =  inp.split()

arr = []
for r in range(int(row)):
    s = input()
    a = list(map(int,s.split()))
    arr.append(a)

my_nump = numpy.array(arr)
print(numpy.transpose(my_nump))
print(my_nump.flatten())
