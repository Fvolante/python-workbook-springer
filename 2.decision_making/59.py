##
# Write a program that reads a date from the user and computes its immediate successor.
# For example, if the user enters values that represent 2019-11-18 then your program
# should display a message indicating that the day immediately after 2019-11-18 is
# 2019-11-19. If the user enters values that represent 2019-11-30 then the program
# should indicate that the next day is 2019-12-01. If the user enters values that represent
# 2019-12-31 then the program should indicate that the next day is 2020-01-01. The
# date will be entered in numeric form with three separate input statements; one for
# the year, one for the month, and one for the day. Ensure that your program works
# correctly for leap years.
#

# user's inputs
year = int(input("Inserisci l'anno: "))
month = int(input("Inserisci il mese: "))
day = int(input("Inserisci il giorno: "))

##################### 
# check leap year
#

# set leap variable
is_leap = False

# leap check
if year % 400 == 0:
    is_leap = True

elif year % 100 == 0:
    is_leap = False

elif year % 4 == 0:
    is_leap = True
    
else:
    is_leap = False

##################### 
# define month days
#     

if month == 11 or \
    month == 4 or \
    month == 6 or \
    month == 9:
    days = 30
elif month == 2:
    if is_leap:
        days = 29
    else:
        days = 29
else:
    days = 31

######################
# compute date
#

# compute next day
next_day = day + 1 if (day + 1) <= days else 1

# compute next month
if next_day != 1:
    next_month = month
else:
    if month + 1 == 13:
        next_month = 1
    else:
        next_month = month + 1

# compute next year
if next_month != 1:
    next_year = year
else:
    if month == 1:
        next_year = year
    else:
        next_year = year + 1

# display result
print("La data inserita è %02d-%02d-%02d" %(day, month, year))
print("La data successiva è %02d-%02d-%02d" %(next_day, next_month, next_year))

