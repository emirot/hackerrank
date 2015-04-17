g = []


def is_son_of_pi(val):
    a = []
    val_pi = "31415926535897932384626433833"
    s = val.split()
    #print("s:",s)
    lee = ""
    for e in s:
        lee += str(len(e))
    print("lee[%s]" % lee)
    print("val[%s]"% val_pi[:len(lee)])
    if lee == val_pi[:len(lee)]:
        g.append("It's a pi song.")
    else:
        g.append("It's not a pi song.")

if __name__ == '__main__':
    nb_test = int(input())
    for i in range(0, nb_test):
        a = str(input())
        is_son_of_pi(a)
    for i in g:
        print(i)
