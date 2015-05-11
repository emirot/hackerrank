

def remove_duplicate_letter_in_keyword(key):
    new_key = ""
    for i in key:
        if i not in new_key:
            new_key += i
    return new_key


def cut_array_key_len(alph, key):
    i = 0
    arr = []
    while len(alph) > 0:
        sub = alph[0:len(key)]
        arr.append(sub)
        alph =  alph[len(key):]
    return arr


def get_vertical_array(arr, item):
    pos =  arr[0].index(item)
    s = ""
    for i in arr:
        if pos < len(i):
            s += i[pos]
    return s

def transposition_cypher(key, to_be_decode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_trim = alphabet
    for e in key:
        alphabet_trim = alphabet_trim.replace(e,"")
    arr = cut_array_key_len(alphabet_trim, key)
    res = sorted(key)
    sort_key =""
    for i in res:
        sort_key += i
    arr.insert(0, key)
    new_string = ""
    for e in sort_key:
        res = get_vertical_array(arr, e)
        new_string += res
    s = ""
    for e in to_be_decode:
        s += return_transposed_letter(alphabet, e, new_string)
    return s.upper()


def return_transposed_letter(alphabet, l, new_alphabet):
    pos = new_alphabet.find(l)
    if pos >= 0:
        return  alphabet[pos]
    return l


if __name__ == '__main__':
    nb_test_case = int(input())
    i =0
    while i < nb_test_case:
        key = input()
        to_be_decode = input()
        key = remove_duplicate_letter_in_keyword(key.lower())
        print(transposition_cypher(key.lower(), to_be_decode.lower()))
        i += 1
