
def array_left_rotation(a, n, k):
    for i in range(0, k):
        re = a.pop(0)
        a.append(re)
    return a

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
