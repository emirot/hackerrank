

def integerSumAnInt(element, arr):
    for i,num in enumerate(arr):
        j = i + 1
        while j < len(arr):
            if (num + arr[j]) == element:
                return True
            j += 1
        print("i", i, "num", num)
    return False


if __name__ == '__main__':
    print(integerSumAnInt(3, [1,3,4,5,56,6,7,7,7,5,33,24]))
    print(integerSumAnInt(4, [1,3,4,5,56,6,7,7,7,5,33,24]))
    print(integerSumAnInt(0, [-1,0,1]))
    print(integerSumAnInt(2, [1,2,3]))
