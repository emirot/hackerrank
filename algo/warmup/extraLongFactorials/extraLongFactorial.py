

def extra_factorial(n):

    if n == 0:
        return 1
    return n * extra_factorial(n-1)


if __name__ == '__main__':
    n =  int(input())
    print(extra_factorial(n))