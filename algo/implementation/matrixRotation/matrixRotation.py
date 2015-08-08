__author__ = 'nolanemirot'
import sys
from copy import deepcopy


# m number of row
# n number of4 column

DEBUG = 0

def rotate_matrix(arr, n , m, r, arr_base):
    #print("M",m)
    speed = False
    v_fast = 0
    iiii = 0
    if r == 0:
        return arr
    if n == 1 and m == 1:
        return arr
    depth = min(n,m)
    if DEBUG==1:
        print(depth)
        print(depth//2)
    if depth % 2 != 0:
        depth -=1
    while iiii < r:
        if speed == True:
            while iiii + v_fast < r:
                iiii += v_fast
                print("Ifast", iiii)
        for sta in range (depth//2):
            if DEBUG:
                print('=========',sta)
            top_left = arr[sta][sta]
            if DEBUG:
                print("top left" , top_left)
            i = sta
            while i < n - 1 - sta:
                arr[sta][i] = arr[sta][i + 1]
                i += 1
            if DEBUG:
                [print(j) for j in arr]

            if DEBUG:
                print('=========',sta)
            j = m - sta
            bot_left = arr[j-1][sta]
            if DEBUG:
                print("bot_left", bot_left)
            while j - 1  > sta:
                arr[j-1][sta] = arr[j-1-1][sta]
                j -= 1

            arr[sta + 1][sta] = top_left # replace top left below
            if DEBUG:
                [print(j) for j in arr]

            botom_right = arr[m-1-sta][n-1-sta]

            if DEBUG:
                print('=========', sta)
                print("botom right", botom_right)
            z = n - 1 - sta
            while z - sta > 0:
                arr[m-1-sta][z] = arr[m-1-sta][z-1]
                z -= 1
            arr[m-1-sta][1+sta] = bot_left
            if DEBUG:
                [print(j) for j in arr]
            if DEBUG:
                print('=========',sta)
            top_right = arr[sta][n-1-sta]
            if DEBUG:
                print("top right", top_right)
            y = 0
            a = m -1
            while y + sta < m -1 -sta:
                arr[y + sta ][n-1-sta] = arr[y + sta + 1][n-1-sta]
                y += 1
            if DEBUG:
                [print(j) for j in arr]
                print("add bot")
            arr[m-1-1-sta][n-1-sta] = botom_right
            if DEBUG:
                [print(j) for j in arr]
                print('=========',sta)
        iiii += 1

        if arr_base == arr:
            speed = True
            v_fast = iiii + 1
            print("NEW_ ARR", arr)
            print("nb_rotation:",iiii)
            #sys.exit(1)
    return arr





def print_p(arr):
    for row in arr:
        print(" ".join(map(str,row)))



def optmize_algorithm(m, n , n_tour):
    mm =  (m-1) * 2
    nn =  (n-1) * 2
    print("mm", mm)
    print("nn", nn)
    one_full_turn = nn + mm
    print("one full trun", one_full_turn)
    n = n_tour % one_full_turn
    return one_full_turn

#optmize_algorithm(4,4,6342)


if __name__ == '__main__':
    arr = []
    arr_res = []
    param_line =  input()
    p = list(map(int, param_line.split()))
    m = p[0]
    n = p[1]
    r = p[2]
    # print("N", n)
    # print("m", m)
    # print("p", r)
    #nb_to_pass = optmize_algorithm(m, n, r)
    for i in range(m):
        line = input()
        arr.append(list(map(int, line.split())))
    arr_base = deepcopy(arr)
    arr_res = rotate_matrix(arr, n, m, r, arr_base)
    if DEBUG:
        print("=======")
    print_p(arr_res)