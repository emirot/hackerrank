from itertools import permutations

line = input()
w, l = line.split()

for i in permutations(sorted(w), int(l)):
    print("".join(i))