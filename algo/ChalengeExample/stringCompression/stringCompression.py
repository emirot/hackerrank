__author__ = 'nolanemirot'


def stringCompression(string):
    s = ""
    i = 0
    count = 0
    end = ""
    while i < len(string)-1:
        if string[i] == string[i+1]:
            count+=1
        else :
            s+= string[i] + str(count+1)
            count = 0
        i+=1
        end = string[i]
    if(string[len(string)-1]== end):
        count+=1
    s += string[i] + str(count)
    print(s)

if __name__ == '__main__':
    stringCompression("aacvvvvvbbbbb")