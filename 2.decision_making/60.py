##
# The following formula can be used to determine the day of the week for January 1
# in a given year:
#
# day_of_the_week = (year + floor((year − 1) / 4) − floor((year − 1) / 100) +
#                   floor((year − 1) / 400)) % 7
#
# The result calculated by this formula is an integer that represents the day of the
# week. Sunday is represented by 0. The remaining days of the week following in
# sequence through to Saturday, which is represented by 6.
# Use the formula above to write a program that reads a year from the user and
# reports the day of the week for January 1 of that year. The output from your program
# should include the full name of the day of the week, not just the integer returned by
# the formula.
#
from math import floor

# user's input
year = int(input("Inserisci l'anno: "))

# formula
day_of_the_week = (year + floor((year - 1) / 4) - \
                        floor((year - 1) / 100) + \
                        floor((year - 1) / 400)) \
                        % 7

# covert number to relative names
if day_of_the_week == 0:
    day_of_the_week = "Domenica"
elif day_of_the_week == 1:
    day_of_the_week = "Lunedì"
elif day_of_the_week == 2:
    day_of_the_week = "Martedì"
elif day_of_the_week == 3:
    day_of_the_week = "Mercoledì"
elif day_of_the_week == 4:
    day_of_the_week = "Giovedì"
elif day_of_the_week == 5:
    day_of_the_week = "Venerdì"
elif day_of_the_week == 6:
    day_of_the_week = "Sabato"

# print result
print("Nell'anno", year,"il 1 Gennaio è", day_of_the_week)