# Link: https://www.hackerrank.com/challenges/day-of-the-programmer
# Time complexity: O(n)
# Week: 2
def dayOfProgrammer(year):
    if year < 1918:
        if year % 4 == 0 :
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year > 1918:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year == 1918:
        return f"25.01.{year}"
    
"""
def dayOfProgrammer(year):
    if year == 1918:
        return f"26.09.{year}"
    
    if ((year < 1918) and (year % 4 == 0)  or (year > 1918) and (year % 4 == 0 and year% 100 != 0 or year % 400 == 0)):
            return f"12.09.{year}"
    else:
            return f"13.09.{year}
"""

"""
def dayOfProgrammer(year):
    if year == 1918:
        return ('26.09.1918')
    elif year<1918 and year%4==0:
        return (f'12.09.{year}')
    elif (year%4==0 and year%100!=0) or (year%400==0):
        return (f'12.09.{year}')
    else:
        return (f'13.09.{year}')
"""

"""
from datetime import date, timedelta

def dayOfProgrammer(year):
    # Write your code here
    days = 268
    if year != 1918:
        days = 255 - ((year % 100) == 0 and year < 1918) 
    return (date(year,1,1) + timedelta(days=days)).strftime("%d.%m.%Y")
"""

"""
def isLeapYear(year, cat):
    
    if cat == 'g':
        return True if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) else False
    
    elif cat == 'j':
        return True if year % 4 == 0 else False
    

def dayOfProgrammer(year):
    
    if year > 1918:
        day = '12' if isLeapYear(year, 'g') else '13'
    elif year < 1918:
        day = '12' if isLeapYear(year, 'j') else '13'
    else:
        day = '26'
        
    return day + '.' + '09' +  '.' + str(year)
"""
