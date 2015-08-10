__author__ = 'nolanemirot'


import re



nb_case = int(input())
arr = []


for i in range(nb_case):
    text =  input()
    arr.append(text)




arr_sub = []
nb_sub_input = int(input())

for i in range(nb_sub_input):
    arr_sub.append(input())


for sub_str in arr_sub:
    t = 0
    for text in arr:
        regex_str = "\w+("+ sub_str +")\w+"
        m = re.findall(regex_str, text)
        t += len(m)
    print(t)

