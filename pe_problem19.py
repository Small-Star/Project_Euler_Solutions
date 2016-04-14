#Project Euler - Problem 19 Solution
#04/13/2016

#Problem: Sundays: Find how many Sundays fell on the first of the month during the 20th century
#Solution Strategy: Brute force

def find_sundays(weekday,year):
    num_sundays = 0

##  Note:
##    Monday = 0
##    Tuesday = 1
##    Wednesday = 2
##    Thursday = 3
##    Friday = 4
##    Saturday = 5
##    Sunday = 6

    month_amounts = []
    base_month_amounts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year_month_amounts = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    #Check for leap year
    if ((year%4 == 0) and not (year%100 == 0)) or (year%400==0):
        month_amounts = leap_year_month_amounts.copy()
    else:
        month_amounts = base_month_amounts.copy()

    for m in month_amounts:
        if (weekday == 6):
            num_sundays += 1
        #Set weekday for the first of next month by calculating (current weekday + number of days in month) mod 7
        weekday = (weekday + m)%7

    return(weekday,num_sundays)
        
def find_sundays_in_range(beg_year,end_year):
    #Note that the range is inclusive
    num_sundays = 0
    
    #Correct for the fact that the given starting point is outside the range of interest
    (weekday,s) = find_sundays(0,1901)
    
    for y in range(beg_year,end_year+1):
        (weekday,s) = find_sundays(weekday,y)
        num_sundays += s

    return num_sundays
        
