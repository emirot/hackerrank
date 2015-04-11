

def iskaprekar(val,origin):
    if val == 1:
        return True
    strval = str(val)
    if len(strval) > 1:
        le = int(len(strval) / 2)
        left = strval[:le]
        right = strval[le:]
        #print("left:",left)
        #print("reight:", right)
        if int(left) + int(right) == origin:
            return True
    return False


def kaprekar(lower_val, upper_val):
    arr = []
    for i in range(lower_val,upper_val+1):
        sqr = i**2
        if iskaprekar(sqr,i):
            arr.append(i)
    if len(arr) == 0:
        print("INVALID RANGE")
    for i in arr:
        print(i,end=" ")




if __name__ == '__main__':
    lower_val = int(input())
    upper_val = int(input())
    kaprekar(lower_val,upper_val)
    # iskaprekar(2025)
    # iskaprekar(81)
