__author__ = 'nolanemirot'



n = int(input())
line = input()
arr = list(map(int, line.split()))
arr.sort()
med = len(arr)//2
print(arr[med])