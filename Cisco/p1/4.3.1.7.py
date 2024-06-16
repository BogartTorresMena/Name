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
        

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
