

def funny_string(s1, s2):
    #print("s1:",s1)
    #print("s2:",s2)
    i = 1
    while i < len(s1):
        if (abs(ord(s1[i-1])-ord(s1[i])) != abs(ord(s2[i-1])-ord(s2[i]))):
            return "Not Funny"
        i += 1
    return "Funny"

if __name__ == '__main__':
    nb_test = int(input())
    for i in range(0, nb_test):
        funny = input()
        print(funny_string(funny, funny[::-1]))
