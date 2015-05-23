__author__ = 'nolanemirot'



def standardize_mobile_number(f):

    def standa(*args, **kwargs):
        x = f(*args, **kwargs)
        a = []
        for i in x:
            i_s = str(i)
            if len(i_s) == 10:
                i_s = "91" + i_s
                a.append(int(i_s))
            elif len(i_s) == 11:
                i_s = "91" + i_s[1:]
                a.append(int(i_s))
            else:
                a.append(i)
        a.sort()
        b = []
        for e in a:
            ss = str(e)
            tmp  = "+91" + " " + ss[2:7]  + " " + ss[7:]
            b.append(tmp)
        return b
    return standa




@standardize_mobile_number
def sort_mobile_number(arr):
    return arr


if __name__ == '__main__':
    nbNum = int(input())
    arr = []
    for i in range(0, nbNum):
        a = int(input())
        arr.append(a)
    #print(arr)
    a = sort_mobile_number(arr)
    for i in a:
        print(i)