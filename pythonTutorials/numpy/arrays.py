import numpy

st = input()
a = list(map(float, st.split()))
b = numpy.array(a[::-1],float)
print(b)
