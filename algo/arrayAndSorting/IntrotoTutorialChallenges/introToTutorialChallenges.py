__author__ = 'nolanemirot'




if __name__ == '__main__':
    V = int(input())
    n = int(input())
    line = input()
    arr = []
    arr = list(map(int,line.split()))
    #print(arr)
    for i,a in enumerate(arr):
        if a ==V:
            print(i)
