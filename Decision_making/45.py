##
# Canada has three national holidays which fall on the same dates each year.
#
# Holiday           Date
# ------------------------------
# New Year’s Day    January 1
# Canada Day        July 1
# Christmas Day     December 25
#
# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.
#

# user's input
month = input("Inserisci il mese: ")
month = month.lower()

day = int(input("Inserisci il giorno: "))

# check holidays
holiday = ""

if month == "gennaio" and day == 1:
    holiday = "Capodanno"
elif month == "luglio" and day == 1:
    holiday = "Canada Day"
elif month == "dicembre" and day == 25:
    holiday = "Natale"

# print result
if holiday == "":
    print("La data non corrisponde ad una festività fissa")
else:
    print("Il", day, month.capitalize(),"è", holiday)    