__author__ = 'nolanemirot'



def ice_cream_parlor(n, arr):

    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if n == arr[i] + arr[j]:
                print(i+1, j+1)
                return
            j += 1
        i += 1




if __name__ == '__main__':
    nb_test_case =  int(input())
    for i in range(nb_test_case):
        M = int(input())
        N = int(input())
        line = input()
        arr = list(map(int, line.split()))
        ice_cream_parlor(M, arr)