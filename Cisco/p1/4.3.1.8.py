def is_year_leap(year):
    if(1582<=year):
        if(year%4!=0):
            return False
        elif(year%100!=0):
            return True
        elif(year%400!=0):
            return False
        else:
            return True

def days_in_month(year, month):
    d=30+(month%2 and month<8)+(1-month%2 and 7<month)
    if month==2:
        d-=2-is_year_leap(year)
    return d

def day_of_year(year, month, day):
    t=0
    for i in range(1,month):
        t+=days_in_month(year,i)
    return t+day

print(day_of_year(2000, 5, 31))
