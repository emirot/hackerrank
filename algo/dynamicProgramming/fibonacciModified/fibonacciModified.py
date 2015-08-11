__author__ = 'nolanemirot'




def fibo_modified(a, b, n):

    i = 2
    while i < n:
        t = b**2 + a
        a = b
        b = t
        i += 1
    print(b)



if __name__ == '__main__':
    a = input()
    arr = list(map(int, a.split()))
    a = arr[0]
    b = arr[1]
    n =  arr[2]
    fibo_modified(a,b,n)