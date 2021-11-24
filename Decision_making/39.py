##
# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed.
#

# user's input
month = input("Inserisci il nome del mese: ")

# initialize a days variable
days = ""

# check months days
if month == "novembre" or \
    month == "aprile" or \
    month == "giugno" or \
    month == "settembre":
    days = "30"
elif month == "febbraio":
    days = "28 o 29"
else:
    days = "31"

# result
print(month, "ha", days, "giorni")
