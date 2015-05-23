__author__ = 'nolanemirot'


x = int(input()) + 1
y = int(input()) + 1
z = int(input()) + 1
N = int(input())

arr = [[X, Y, Z] for X in range(x) for Y in range(y) for Z in range(z) if X + Y + Z != N]

print(arr)