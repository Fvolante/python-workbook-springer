##
# At a particular company, employees are rated at the end of each year. The rating scale
# begins at 0.0, with higher values indicating better performance and resulting in larger
# raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
# between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
# with each rating is shown in the following table. The amount of an employee’s raise
# is $2,400.00 multiplied by their rating.
#
#   Rating          Meaning
#   ----------------------------------------
#   0.0             Unacceptable Performance
#   0.4             Acceptable Performance
#   0.6 or more     Meritorious Performance
#
# Write a program that reads a rating from the user and indicates whether the performance
# for that rating is unacceptable, acceptable or meritorious. The amount
# of the employee’s raise should also be reported. Your program should display an
# appropriate error message if an invalid rating is entered.
#

# user's input
rating = float(input("Inserisci la tua valutazione: "))

# ratings constants
UNACCEPTABLE = 0.0
ACCEPTABLE = 0.4
MERITORIOUS = 0.6

# set meaning and pay raise variable
meaning = ""
pay_raise = 0

if rating == UNACCEPTABLE:
    meaning = "inaccettabile"
    pay_raise = 2400 * UNACCEPTABLE

elif rating == ACCEPTABLE:
    meaning = "accettabile"
    pay_raise = 2400 * ACCEPTABLE

elif rating >= MERITORIOUS:
    meaning = "meritoria"
    pay_raise = 2400 * MERITORIOUS

else:
    print("La valutazione inserita non esiste")

if meaning != "":
    print("Secondo la tua valutazione hai eseguito una performance", meaning)
    print("Il tuo stipendio avrà un aumento di %.2f euri" %pay_raise)