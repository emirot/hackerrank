L = []


def insert(a,b):
    L.insert(a,b)

def reverse():
    L.reverse()

def extend(arr):
    L.extend(arr)
    
def append(a):
    L.append(a)
    
def my_print():
    print(L)

def is_known_kewword(key):
    if key in ['insert','print', 'remove', 'append', 'pop', 'append', 'reverse']:
        return True
    return False

def remove(a):
    L.remove(a)
    
def sort():
    L.sort()
    
def pop():
    L.pop()

def operation_on(arr):

    if len(arr) == 1:
        if arr[0] == 'print':
            my_print()
        else:
            eval(arr[0])()
    if len(arr) == 2:
        eval(arr[0])(int(arr[1]))
    if len(arr) == 3:
        eval(arr[0])(int(arr[1]),int(arr[2]))

if __name__ == '__main__':
    nb_case = int(input())
    for i in range(nb_case):
        line = input()
        arr = line.split()
        operation_on(arr)
        
    
        
            
    
        
        
