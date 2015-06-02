__author__ = 'nolanemirot'


one_num = {0:"zero",1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",7:"seven", 8:"eight",9:"nine",

10:"ten", 11:"eleven" , 12:"twelve",13:"thirteen",  14: "fouteen", 15: "fifteen", 16:"sixteen", 17:"seventeen",
           18:"eighteen", 19:"nineteen"}

dix = {20: "twenty", 30:"thirty", 40:"forty", 50:"fifty"}


def create_num(minu):
    mi = minu % 10
    diz = int(minu / 10)
    if mi==0:
        return dix[diz*10]
    return dix[diz*10] + " " + one_num[mi]

def the_time_in_hour(hour, minu):
    if hour >= 0 and minu==0:
        return one_num[hour] + " " + "o' clock"

    if hour >=0 and minu==15:
        return "quarter past "+ one_num[hour]

    if hour >= 0 and minu==30:
        return "half past " + one_num[hour]

    if hour >= 0 and (minu < 30 and minu >0):
        if len(str(min)) ==2 and minu >= 20:
           return create_num(minu) +" minutes past "+ one_num[hour]
        return one_num[minu]+" minutes past "+ one_num[hour]
    if hour >=0 and minu==45:
        return "quarter to "+ one_num[hour+1]

    if hour >= 0 and (minu > 30):
        if len(str(min)) ==2 and minu <= 40:
            return create_num(60-minu) +" minutes to "+ one_num[hour+1]
        return one_num[60-minu] + " minutes to " + one_num[hour+1]





if __name__ == '__main__':
    hour = int(input())
    min = int(input())
    print(the_time_in_hour(hour, min))