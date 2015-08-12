__author__ = 'nolanemirot'


import collections



def find_diff_anagram():
    line = input()
    if len(line) % 2 != 0:
        print(-1)
        return
    else:
        cut = len(line) // 2
        #print(cut)
        a = line[:cut]
        b = line[cut:]
    # print("a",a)
    # print("b",b)
    cnt_a = collections.Counter(a)
    cnt_b = collections.Counter(b)
    t = 0
    res = cnt_b - cnt_a
    if not res:
        print(0)
    else:
        #print("res", res)
        for i in res:
            t += res[i]
        print(t)


if __name__ == '__main__':
    nn_case = int(input())
    for i in range(nn_case):
        find_diff_anagram()
