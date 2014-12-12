__author__ = 'nolan'

if __name__ == '__main__':
    line = input()
    tmp = list(map(int,line.split()))
    nbItems = tmp[0]
    money = tmp[1]
    lineToys = input()
    arr = list(map(int, lineToys.split()))
    arr.sort()
    #print(arr)
    totalPrice =0
    i = 0
    a = 0
    while totalPrice < money and i < len(arr):
        totalPrice += arr[i]
        if(totalPrice < money):
            a +=1
        i+=1
    print(a)