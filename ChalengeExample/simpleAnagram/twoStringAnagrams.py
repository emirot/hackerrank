__author__ = 'nolanemirot'




def isAnagram(str1, str2):
    if(len(str1)!=len(str2)):
        return False
    s1 = sorted(str1)
    s2 = sorted(str2)
    if s1 == s2:
        return True
    else:
        return False




if __name__ == '__main__':
    print(isAnagram("string","gtrins"))
    print(isAnagram("string","notSameAtAll"))
    print(isAnagram("hallo","hello"))