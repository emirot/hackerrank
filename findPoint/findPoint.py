__author__ = 'nolanemirot'





def findPoint(arr):
    px = arr[0]
    py = arr[1]
    qx = arr[2]
    qy = arr[3]
    resX = (qx - px) + qx
    resY = (qy - py) + qy
    print(resX,resY)

if  __name__ == '__main__':
    nbTestCase = int(input())
    i = 0
    while i < nbTestCase:
        line = input()
        arr = line.split()
        results = list(map(int, arr))
        findPoint(results)
        i += 1