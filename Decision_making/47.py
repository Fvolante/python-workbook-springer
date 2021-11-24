##
# The year is divided into four seasons: spring, summer, fall (or autumn) and winter.
# While the exact dates that the seasons change vary a little bit from year to year
# because of the way that the calendar is constructed, we will use the following dates
# for this exercise:
#
#   Season      First Day
#   -------------------------
#   Spring      March 20
#   Summer      June 21
#   Fall        September 22
#   Winter      December 21
#
# Create a program that reads a month and day from the user. The user will
# enter the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered
#

# take 2 inputs from user 
month, day = input("Inserisci il mese e il giorno: ").split()

# convert day to int
day = int(day)

# check sicure season months
if month == "aprile" or month == "maggio": 
    season = "Primavera"
elif month == "luglio" or month == "agosto":
    season = "Estate"
elif month == "ottobre" or month == "novembre":
    season = "Autunno"
elif month == "gennaio" or month == "febbraio":
    season = "Inverno"
else:
# check season for ambiguous months
    if month == "marzo" and day >= 20:
        season = "Primavera"
    elif  month == "marzo" and day < 20:
        season = "Inverno"
    elif  month == "giugno" and day >= 21:
        season = "Estate"
    elif  month == "giugno" and day < 21:
        season = "Primavera"
    elif  month == "settembre" and day >= 22:
        season = "Autunno"
    elif  month == "settembre" and day < 22:
        season = "Estate"
    elif  month == "dicembre" and day >= 21:
        season = "Inverno"
    elif  month == "dicembre" and day < 21:
        season = "Autunno"

# print result
print("La stagione è", season)