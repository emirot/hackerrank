import calendar

a = input()
arr = a.split()

day =calendar.day_name[calendar.weekday(int(arr[2]),int(arr[0]), int(arr[1]))].upper()
print(day)
