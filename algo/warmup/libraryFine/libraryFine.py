

def library_fine():
    line_ret = input()
    ret = list(map(int,line_ret.split()))
    day_ret = ret[0]
    month_ret = ret[1]
    year_ret = ret[2]
    line_pick = input()
    p = list(map(int, line_pick.split()))
    day_pick = p[0]
    month_pick = p[1]
    year_pick = p[2]
    if year_pick == year_ret and month_pick == month_ret and day_pick < day_ret:
        day_dif = day_ret - day_pick
        return(day_dif*15)
    if year_pick == year_ret and month_pick < month_ret:
        month_dif = month_ret - month_pick
        return(month_dif * 500)
    if year_ret > year_pick:
        return 10000
    return 0







if __name__ == '__main__':
    print(library_fine())