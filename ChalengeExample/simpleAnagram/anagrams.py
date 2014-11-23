__author__ = 'nolanemirot'



def anagrams(word):
    if len(word) < 2:
        return word
    else:
        tmp = []
        for i, letter in enumerate(word):
            print("letter:",letter,"word[:i]",word[:i]," word[i+1:]",word[i+1:])
            li = anagrams(word[:i]+word[i+1:])
            print(li)
            print("========")

            for l in li:
                tmp.append(letter+l)
        return tmp

if __name__ == '__main__':
    a = anagrams("abc")
    print(a)