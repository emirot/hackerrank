__author__ = 'nolanemirot'
import re


def convertime():
    line =  input()
    pm_am = line[-2:]
    if pm_am == 'PM':
        if line[0:2] == '12':
            return line[0:8]
        a = line[0:2]
        a = int(a) + 12
        return(str(a)+line[2:8])
    elif pm_am == 'AM':
        if line[0:2] == '12':
            return '00'+line[2:8]
        return(line[0:8])
    else:
        print("Error")




if __name__ == '__main__':
    print(convertime())