##
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.
#

IVA = 10
TIP = 18

cost = float( input("Inserisci il costo del pasto in euri: ") )

iva_cost = cost / IVA
tip_cost = cost / TIP

total = cost + iva_cost + tip_cost

print("Il conto totale, comprensivo di iva (", "%.2f" %iva_cost, "euri) e mancia (", "%.2f" %tip_cost, "euri), è di:", "%.2f" %total, "euri")