
nb_test = int(input())

r = []
for i in range(nb_test):
    line = input()
    r.append(line.split())

for e in r:
    try:
        res = int(e[0]) // int(e[1])
    except Exception as e:
        print("Error Code: {}".format(str(e)))
    else:
        print(res)
