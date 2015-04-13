import sys

def is_prime(num):
    count = 0
    if num in arr:
        return True
    if num  < 2:
        return False
    for i in range (2, num):
        if num % i == 0:
            return False
    return True




def find_prime_factors(num):
    arr = []
    i = 2
    while i < num:
        if is_prime(i):
            if num % i == 0:
                num = int(num / i)
                arr.append(i)
                #print("num", num)
                i =2
        i = i + 1
    arr.append(int(num))
    return arr


if __name__ == '__main__':
    a = []
    arr = []
    val = int(input())
    if val == 1 :
        print("0")
        sys.exit(0)
    arr = find_prime_factors(val)
    c = 0
    for i in arr:
        ii = str(i)
        for l in ii:
            c += int(l)
    st = str(val)
    a = 0
    for i in st:
        a += int(i)
    if a==c:
        print("1")
    else:
        print("0")

#not passing 4937775 -> 0 timeout
#not passing 22050918644 -> 1 timeout
