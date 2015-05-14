
def strange_grid(x, y):
    val = 0
    first_row =  [ 0,  2, 4,  6,  8]
    if y % 2 == 0:
        if y == 0:
            return first_row[x - 1]
        val = first_row[x - 1]
        val = val + ( 10 * (y//2)) -10
        return val + 1
    else:
        val = first_row[x - 1]
        val = val + ( 10 * (y//2))
        return val
        

if __name__ == '__main__':
    line = input()
    arr = list(map(int, line.split()))
    y = arr[0]
    x = arr[1]
    print(strange_grid(x, y))
