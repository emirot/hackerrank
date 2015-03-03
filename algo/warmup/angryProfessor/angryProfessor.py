__author__ = 'nolanemirot'



def classGetCanceled(N,K, arr):
    nbOnTime = 0
    for i in arr:
        if i <= 0 :
            nbOnTime += 1
    if nbOnTime >= K:
        return "NO"
    return "YES"


if __name__ == '__main__':
    nbTestCase = int(input())
    for i in range(nbTestCase):
        line = input()
        arr = list(map(int, line.split()))
        N = arr[0]
        K = arr[1]
        studentLine = input()
        students = list(map(int, studentLine.split()))
        print(classGetCanceled(N,K, students))