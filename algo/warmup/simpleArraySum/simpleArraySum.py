
a = input()
b = input()

arr = list(map(int,b.split()))

res = 0
for i in arr:
    res += i
print(res)