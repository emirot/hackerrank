__author__ = 'nolanemirot'
import math



def create_n_m_matrix(n, m):
    arr = []
    i =0
    while i < n:
        j = 0
        a = ['' for j in range(m)]
        arr.append(a)
        i += 1
    #[print(a) for a in arr]
    return arr


def fill_matrix(arr, line):
    a = 0
    for i in range(len(arr)):
        j = 0
        while j < len(arr[i]):
            if a < len(line):
                ll = line[a]
            else:
                ll = ''
            arr[i][j] = ll
            j += 1
            a += 1
    #[print(a) for a in arr]
    return arr



def traverse_by_column(arr):
    y = 0
    x = 0
    res = []
    while x < len(arr[0]):
        y = 0
        r = ""
        while y < len(arr):
            if arr[y][x] != '':
                r += arr[y][x]
            y += 1
        res.append(r)
        x += 1
    print(" ".join(x for x in res))


def check_flo_ceil(flo, cel, len_line):
    if flo * cel < len_line and flo < cel:
        flo += 1
    return flo, cel


if __name__ == '__main__':
    line = input()
    line = line.replace(" ", "")
    len_line = len(line)
    squ = math.sqrt(len_line)
    flo = math.floor(squ)
    cei = math.ceil(squ)
    #print("flor", flo)
    #print("ceoil", cei)
    flo, cei = check_flo_ceil(flo, cei, len_line)
    arr = create_n_m_matrix(flo, cei)
    arr = fill_matrix(arr, line)
    traverse_by_column(arr)
