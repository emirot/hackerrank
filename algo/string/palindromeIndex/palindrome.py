import math



def isPalindrome(str):
    i = 0
    mid = math.ceil(len(str)/2)
    end = len(str) -1
    while(i != mid):
        if(str[i] != str[end -i]):
            if (str[i+1]==str[end-i]) and (str[i+2]==str[end-i-1]):
                return i
            if(str[i] == str[end-1-i] ):
                return end  -i
        i += 1
    return -1



nbTestCase = int(input())
i = 0
while i < nbTestCase:
    str = input()
    print(isPalindrome(str))
  #  print(str[::-1])
    i += 1