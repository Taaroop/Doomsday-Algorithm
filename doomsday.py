# Doomsday Algorithm

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

def day(date, month, year):
    leap_count = 0
    
    closest_century = year - (year%100)
    
    if closest_century % 400 == 0:
        doomsday_century = 2
    elif closest_century % 400 == 300:
        doomsday_century = 3
    elif closest_century % 400 == 200:
        doomsday_century = 5
    elif closest_century % 400 == 100:
        doomsday_century = 0
        
    for y in range(closest_century+1, year+1):
        if is_leap(y) == True:
                leap_count += 1
    
    plus = year - closest_century + leap_count
    doomsday = (doomsday_century + plus) % 7
    
    li_month_doomsday = [3, 28, 14, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    
    if is_leap(year) == True:
        li_month_doomsday[0] += 1
        li_month_doomsday[1] += 1
    
    month -= 1
    know = li_month_doomsday[month]
    days_between = abs(date-know)
    day = (doomsday + days_between)%7
    return ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'][day]

print(day(16, 12, 1971))
