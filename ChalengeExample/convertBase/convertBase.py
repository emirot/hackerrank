__author__ = 'nolanemirot'




def toDigits(n, b):
    """Convert a positive number n to its digit representation in base b."""
    digits = []
    while n > 0:
        digits.insert(0,n % b)
        n  = n // b
    return digits


def fromDigits(digits, b):
    """Compute the number given by digits in base b."""
    n = 0
    for d in digits:
        n = b * n + d
    return n


def compareBits():
    a = 0b010101
    b = 0b101010
    if(a & b == 0):
        print("yes")




if __name__ == '__main__':
    #print(toDigits(10,2))
    compareBits()
