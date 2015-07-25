import collections

a = input()
b = input()


cnt_a = collections.Counter(a)
cnt_b =  collections.Counter(b)


min_val = (cnt_a & cnt_b)

x = 0

#common in both string
for k,v  in min_val.items():
    print(" ", k, ":", v)
    x += v

print((len(a) - x) + (len(b) - x))


