__author__ = 'nolanemirot'



def calcGrade(name, dic):
    arr = dic[name]
    val = 0.00
    for i in arr:
        val += i
    print(format(val/len(arr), '.2f'))



if __name__ == '__main__':
    dic = {}
    nbStudent =  int(input())
    for i in range(0,nbStudent):
        line = input()
        arr = line.split()
        marks = list(map(float,arr[1:]))
        dic[arr[0]] = marks
    name = input()
    calcGrade(name,dic)
