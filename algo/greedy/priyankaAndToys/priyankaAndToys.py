__author__ = 'nolanemirot'



def inRange(el, t):
    if el >= t and el <= (t + 4) :
        return True
    return False

def findNumberToBuy(arr):
    arr = sorted(arr)
    print(arr)
    tmp = []
    nb = 1
    deb = arr[0]
    for el in arr:
        if inRange(el,deb):
            print("range",el)
        else:
            deb = el
            nb += 1
    print(nb)





if __name__ == '__main__':
    nbNumber =  int(input())
    line = input()
    arr = list(map(int,line.split()))
    findNumberToBuy(arr)