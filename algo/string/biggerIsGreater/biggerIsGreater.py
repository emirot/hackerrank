
def find_closer_above(arr):
    v =  arr[0][1]
    i = 0
    res= []
    while i < len(arr):
        a = arr[i][1] - v
        if a > 0:
           res.append([arr[i],i])
        i +=1
    mimi =  min(res)
    mimi = mimi[1]
    tmp =  arr[0]
    arr[0] = arr[mimi]
    arr[mimi] = tmp
    ss = sorted(arr[1:])
    n_arr = [arr[0]] + ss
    return n_arr


def check_for_no_sol(res):
    if sorted(res, reverse=True) == res:
        return True
    return False



def find_lexigo_upper(line):
    res = []
    pos = 0

    for i in line:
        res.append([i, ord(i)])
    i = len(res)
    if check_for_no_sol(res):
        return "no answer"
    while i  > 1:
        if  res[i-2][1] < res[i-1][1] :
            pos = i -2
            break
        i -= 1

    left = res[:pos]
    right = res[pos:]
    ab = find_closer_above(right)
    abc = left + ab
    s = ""
    for i in abc:
        s += i[0]
    return s


if __name__ == '__main__':
    lines = []
    nb_case = int(input())
    for i in range(nb_case):
        lines.append(input())
    for l in lines:
        r = find_lexigo_upper(l)
        print(r)

