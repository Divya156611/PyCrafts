#Method 1 :using function and conditional statement

def days_in_month(month,year):
    if month==2:
        if Year%4==0:
            if Year%100==0:
                if Year%400==0:
                    print(f"29 days in month {month},year {year}")
                else:
                    print(f"28 days in month {month},year {year}")
            else:
                print(f"29 days in month {month},year {year}")
        else:
            print(f"28 days in month {month},year {year}")
    elif month==1 or month in range(3,13,2):
        return f"31 days in month {month},year {year}"
    else:
        return f"30 days in month {month},year {year}"
Month=int(input("Enter the month number:"))
Year=int(input("Enter the year :"))
print(days_in_month(month=Month , year=Year))


#Method 2 : using list & function & conditional statement

def leap_year(year):
        if Year%4==0:
            if Year%100==0:
                if Year%400==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
def days_of_month(month,year):
    days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(month) and month==2:
        return f"29 days in month {month}, year {year}"
    else:
        return f"{days[month-1]} days in month {month},year {year}"
Month=int(input("Enter the month number:"))
Year=int(input("Enter the year :"))
print(days_of_month(month=Month , year=Year))
