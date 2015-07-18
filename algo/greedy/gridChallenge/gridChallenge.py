__author__ = 'nolanemirot'




def gridChallenge(arr):
    tmp = 'a'
    for e in arr:
        if tmp <= e:
            tmp = e
        else:
            return False
    return True



def checkColumn(arr, wl):

    x = 0
    while x < wl:
        y = 0
        tmp = 'a'
        while y < wl:
            elemen = arr[y][x]
            if tmp <= elemen:
                tmp = elemen
            else:
                return False
            y += 1
        x += 1
    return True




if __name__ == '__main__':
    nb_test_case =  int(input())

    for i in range(nb_test_case):
        size = int(input())
        l = ""
        c = []
        for e in range(size):
            line = input()
            a = gridChallenge(sorted(line))
            b = sorted(line)
            c.append(b)
            if a == "NO":
                print(a)
                break
        if checkColumn(c, size):
            print("YES")
        else:
            print("NO")

