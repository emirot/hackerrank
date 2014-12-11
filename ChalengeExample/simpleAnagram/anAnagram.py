__author__ = 'nolanemirot'


def anagram(str):
    if(len(str)< 2):
        return str
    else:
        tmp = []
        for i, sub in enumerate(str):
            s = anagram(sub[i:] + sub[i+1:])
            for a in s:
                tmp.append(a+sub)
    return tmp


if __name__ == '__main__':
    ar = anagram("abc")
    print(ar)