import numpy

a = input()
arr = list(map(int, a.split()))
v = numpy.reshape(arr,(3,3))
print(v)
