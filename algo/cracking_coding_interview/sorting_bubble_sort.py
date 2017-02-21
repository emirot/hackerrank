


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


is_sorted = False
nb_swap = 0

while is_sorted != True:
    i = 0
    is_sorted = True
    while i < len(a) -1:
        if a[i] > a[i+1]:
            tmp = a[i+1]
            a[i + 1] = a[i]
            a[i] = tmp
            is_sorted = False
            nb_swap += 1
        i += 1
        
print("Array is sorted in {} swaps.".format(nb_swap))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[len(a)-1]))

        
