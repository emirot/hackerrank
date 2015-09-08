from itertools import product


line = input()
l =  list(map(int,line.split()))

line = input()
l2 =  list(map(int,line.split()))


for i in product(l, l2):
    print(i, end=" ")