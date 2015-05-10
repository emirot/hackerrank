


def fibonacci(num):
    i = 0
    arr = []

    if num == 0:
        return 0
    if num == 1:
        return 1

    while i <= num:
        if i < 2:
            arr.append(i)
        else:
            arr.append((arr[i-1]) + arr[i-2])
        i += 1

    return arr[len(arr)-1]





def fibonnaci_rec(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibonnaci_rec(num-1) + fibonnaci_rec(num -2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))

print("--------------------------")
print(fibonnaci_rec(0))
print(fibonnaci_rec(1))
print(fibonnaci_rec(2))
print(fibonnaci_rec(3))
print(fibonnaci_rec(4))
print(fibonnaci_rec(5))
print(fibonnaci_rec(6))
print(fibonnaci_rec(7))
