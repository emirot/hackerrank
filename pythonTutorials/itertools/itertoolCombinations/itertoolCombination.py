from itertools import combinations

line = input()
w, l = line.split()
l = int(l)

for j in range(1,l+1):
    for i in combinations(sorted(w), j):
        print("".join(i))