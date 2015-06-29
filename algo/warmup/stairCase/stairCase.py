


def fill_line(nb_p, nb_s):
    a = []
    for i in range(nb_s):
        a.append(' ')
    for i in range(nb_p):
        a.append('#')
    return a



def print_(arr):
    for i in arr:
        for a in i:
         print(a,end='')
        print()

if __name__ == '__main__':
    nb_stair_f = int(input())
    arr = []
    nb_stair = nb_stair_f
    while nb_stair > 0:
        p = nb_stair_f - nb_stair
        arr.insert(0, fill_line(nb_stair, p))
        nb_stair -= 1
    print_(arr)