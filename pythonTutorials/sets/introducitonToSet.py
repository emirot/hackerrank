import sys
nb_v = int(input())

print("nb_v", nb_v,file=sys.stderr)
line = input()

arr = [int(x) for x in line.split()]

print("set_", set(arr),file=sys.stderr)
print(sum(set(arr))/len(set(arr)))
