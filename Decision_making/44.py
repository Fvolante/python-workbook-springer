##
# It is common for images of a country’s previous leaders, or other individuals of historical
# significance, to appear on its money. The individuals that appear on banknotes
# in the United States are listed in below
#
#   Individual              Amount
#   -------------------------------
#   George Washington       $1
#   Thomas Jefferson        $2
#   Abraham Lincoln         $5
#   Alexander Hamilton      $10
#   Andrew Jackson          $20
#   Ulysses S. Grant        $50
#   Benjamin Franklin       $100
#
# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the
# banknote of the entered amount. An appropriate error message should be displayed
# if no such note exists.
#

# user's amount
amount = int(input("Inserisci l'ammontare della banconota in $: "))

# create variable
individual = ""

if amount == 1:
    individual = "George Washington"
elif amount == 2:
    individual = "Thomas Jefferson"
elif amount == 5:
    individual = "Abraham Lincoln"
elif amount == 10:
    individual = "Alexander Hamilton"
elif amount == 20:
    individual = "Andrew Jackson"
elif amount == 50:
    individual = "Ulysses S. Grant"
elif amount == 100:
    individual = "Benjamin Franklin"
else:
    print("Taglio di banconota non riconosciuto")

if individual != "":
    print("Il taglio da", amount, "dollari ha raffigurato", individual)



