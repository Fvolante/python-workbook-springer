##
# Write a function that determines howmany days there are in a particular month. Your
# function will take two parameters: The month as an integer between 1 and 12, and
# the year as a four digit integer. Ensure that your function reports the correct number
# of days in February for leap years. Include a main program that reads a month and
# year from the user and displays the number of days in that month. You may find your
# solution to Exercise 58 helpful when solving this problem.
#

from es91 import monthDays

def main():
    month = int(input("Inserisci il mese (come intero da 1 a 12): "))
    year = int(input("Inserisci l'anno: "))

    print("Il mese selezionato ha:", monthDays(month, year), "giorni")

main()