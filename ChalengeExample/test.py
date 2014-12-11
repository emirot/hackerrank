__author__ = 'nolanemirot'


def function_sqrt(n):
    oldguess = -1
    guess = 1
    while abs(guess-oldguess) > 1:
        oldguess = guess
        guess = (guess + n/guess) / 2
    return guess

a = function_sqrt(36)
print(a)