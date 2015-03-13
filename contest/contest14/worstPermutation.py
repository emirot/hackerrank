__author__ = 'nolanemirot'



def printMe(tab):
    for el in tab:
        print(el,end=" ")


def worstPermutation(k, tab):
    i = 0
    #print("k",k)
    max = sorted(tab)
    max = max[::-1]
    #print("mac",max)
    if k > 0:
        while k > 0 and i < len(tab):
                j = i + 1


                while k > 0 and j < len(tab):
                    #print("tab[i]",tab[i])
                    #print("tab[j]",tab[j])
                    if k > 0:
                        if tab[i] < tab[j] and tab[j] >= max[0]:
                            tmpi = tab[i]
                            tab[i] = tab[j]
                            tab[j] = tmpi
                            max.pop(0)
                            #print("mac",max)
                            #print(tab)
                            k -= 1
                            i = -1
                            j =0
                            break
                    j += 1
                i += 1
        return(tab)



if __name__ == '__main__':
    firstLine  = input()
    arr = []
    arr = list(map(int, firstLine.split()))
    maxPermutation = arr[1]

    secondLine = input()
    tab = []
    tab = list(map(int, secondLine.split()))
    a = worstPermutation(maxPermutation, tab)
    printMe(a)