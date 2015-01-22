__author__ = 'nolanemirot'
import  re


if __name__ == '__main__':
    nbTest = int(input())
    count =0
    for i in range(0,nbTest):
        given = input()
        if re.search("hackerrank", given,re.IGNORECASE):
            count += 1
    print(count)