'''
2. Write an if statement to determine whether a variable holding 
a year is a leap year.
'''

def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  return False

for i in range(2000,3000):
  if is_leap_year(i):
    print (i)