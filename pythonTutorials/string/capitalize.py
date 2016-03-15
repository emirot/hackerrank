line =  input()

i = 0
new = ""
while i < len(line):
    if i == 0 or (i > 0 and line[i-1]==" "):
        new += line[i].capitalize()
    else:
        new += line[i]
    i+=1
    
print(new)
