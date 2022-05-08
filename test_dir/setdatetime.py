import random

def sorting_feb(y):
    if ((y%4 ==0) and (y%100 != 0) or y% 400 ==0) :
        return 29
    else: return 28
    
def set_datetime():
    
    year = 2022
    ran_month = random.randint(1,12)
    ran_day = random.randint(1,31)
    ran_hour = random.randint(0,23)
    ran_min = random.randint(0, 59)

    strMonth =""
    strDay = ""
    strHour = ""
    strMin =""
    start_dt = ""
    end_dt = ""
    month30 = [4,6,9,11]
    if ran_month < 10 :
        strMonth = "0" + str(ran_month)
    else:
        strMonth = str(ran_month)

    if ran_day < 10:
        strDay = "0" + str(ran_day)
    elif ran_day >= 31:
        # 2 월 경우
        if ran_month == 2:
            ran_day = sorting_feb(year)
    # 30일 까지인 경우
        else:    
            for m in month30:
                if ran_day == m:
                    ran_day = 30
                    break
        strDay = str(ran_day)
    else: strDay = str(ran_day)

    if ran_hour < 10:
        strHour = "0" + str(ran_hour)
    else: strHour = str(ran_hour)
    if ran_min < 10:
        strMin = "0" + str(ran_min)
    else: strMin = str(ran_min)
    start_dt = str(year) + strMonth + strDay + strHour + strMin
    if ran_hour + 1 >= 24 :
        end_dt = start_dt
    else:
        end_dt = str(year) + strMonth + strDay + str(int(strHour)+1) + strMin
    
    test_datetime = start_dt +"$" + end_dt
    return test_datetime
