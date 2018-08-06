#Chapter 4: Determining Leap Years

#divisible by 4 but not by 100 or if it is divisible by 400.

year = eval(input("Enter a year to determine if leap year or not: \n"))

isALeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

if isALeapYear ==  True:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
