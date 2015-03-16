__author__ = 'nolanemirot'


l = input()
line = input()
arr  = list(map(int,line.split()))
set1 =set(arr)
#print(arr)

l2 = input()
line2 = input()
arr2  = list(map(int,line2.split()))
set2 = set(arr2)
#print(set2)

a = set1.difference(set2)
#print(a)
b = set2.difference(set1)
#print(b)
a = a.union(b)


for el in sorted(a) :
    print(el)
