


def find_diagonal_difference(a):
    i = 0
    j = 0
    d1 = []
    while i < len(a):
        d1.append(a[i][j])
        i += 1
        j += 1
    x = 0
    i = 0
    d2 = []
    while i < len(a):
        b = len(a[i]) - x
        d2.append(a[i][b-1])
        x += 1
        i += 1

    print(abs(sum(d1)-sum(d2)))

if __name__ == '__main__':
    a = []
    nb_line = int(input())
    for i in range(0, nb_line):
        line = input()
        l = list(map(int, line.split()))
        a.append(l)
    find_diagonal_difference(a)