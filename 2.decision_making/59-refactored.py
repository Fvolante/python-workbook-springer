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

from datetime import date, timedelta

# user's inputs
year = int(input("Inserisci l'anno: "))
month = int(input("Inserisci il mese: "))
day = int(input("Inserisci il giorno: "))

# use built in functions
date = date(year, month, day)
next_date = date + timedelta(days = 1)

# print result
print("La data inserita è:", date)
print("La data successiva è:", next_date)