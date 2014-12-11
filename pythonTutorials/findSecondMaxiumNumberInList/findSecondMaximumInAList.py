__author__ = 'nolan'

if __name__ == '__main__':
    n = input()
    line = input()
    arr = list(map(int,line.split()))
    max = arr[0]
    max2 = arr[0]
    for el in arr:
        if el > max:
            max = el
    for el in arr:
        if el != max and (max2 < el or max2 == max):
            max2 = el
    print(max2)
