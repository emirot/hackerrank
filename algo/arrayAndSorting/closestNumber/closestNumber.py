
arr = []
N = int(input())
line = input()
arr = list(map(int,line.split() ))


arr.sort()
#print("arr:", arr)

i = 0
dif = 0
minu = 0
if len(arr) >= 2:
    minu = arr[1] - arr[0]


pair = []
while i < len(arr) - 1:
    dif = arr[i+1] - arr[i]
    if dif == minu:
        pair.append([arr[i], arr[i+1]])
    if dif < minu:
        pair = []
        minu = dif
        pair.append([arr[i], arr[i+1]])

    i += 1


for i in pair:
    [print(j, end=" ") for j in i]