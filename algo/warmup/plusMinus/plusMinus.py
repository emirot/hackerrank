__author__ = 'nolanemirot'


if __name__ == '__main__':
    pos = 0
    zero = 0
    neg = 0
    nb_val = int(input())
    line = input()
    a = list(map(int,line.split()))
    for i in a:
        if i > 0:
            pos += 1
        if i == 0:
            zero += 1
        if i < 0:
            neg += 1
    print("%.3f" % (pos/nb_val))
    print("%.3f" % (neg/nb_val))
    print("%.3f" % (zero/nb_val))