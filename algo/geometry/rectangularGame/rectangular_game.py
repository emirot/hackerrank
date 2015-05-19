

def draw_cube(maxX, maxY):
    arr = []
    for y in range(maxY):
        tmp = []
        for x in range(maxX):
            tmp.append(0)
        arr.append(tmp)
    return arr

def print_max_number(nb_value, arr_value, arr_set):
    max = 0
    for i in range(0,nb_value):

        arr = arr_value.pop(0)
        # print("arr:", arr)
        count = 0
        for y in range(arr[0]):
            for x in range(arr[1]):
                if arr_set[y][x] == max:
                    count += 1
                arr_set[y][x] += 1
        max +=1
        for aa in arr_set:
            print("arr_set:",aa)
        print("count:", count)
    return count

if __name__ == '__main__':
    arr = []
    nb_cases = int(input())
    for i in range(0, nb_cases):
        line = input()
        vals = list(map(int, line.split()))
        arr.append(vals)

    ys = [arr[x][0] for x in range(0,len(arr))]
    xs = [arr[x][1] for x in range(0,len(arr))]
    print("ys", (ys))
    print("xs", (xs))
    print("ys", max(ys))
    print("xs", max(xs))

    print(min(ys)*min(xs))
