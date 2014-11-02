

n = int(input())
k = int(input())

i = 0
lines = []
while(i < n):
    val = int(input())
    lines.append(val)
    i += 1
lines.sort()
#print(lines)
j=0
arr = []
while(j + k < len(lines)):
    c = j + k - 1
    v = lines[c] - lines[j]
 #   print("line[c]:",lines[c])
 #   print("line[j]",lines[j])
 #   print("v:",v)
    arr.append(v)
    j += 1

print(min(arr))
