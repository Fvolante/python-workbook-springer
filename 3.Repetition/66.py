##
# February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
# Mint. Now that pennies have been phased out retailers must adjust totals so that they
# are multiples of 5 cents when they are paid for with cash (credit card and debit card
# transactions continue to be charged to the penny). While retailers have some freedom
# in how they do this, most choose to round to the closest nickel.
# Write a program that reads prices from the user until a blank line is entered.
# Display the total cost of all the entered items on one line, followed by the amount
# due if the customer pays with cash on a second line. The amount due for a cash
# payment should be rounded to the nearest nickel. One way to compute the cash
# payment amount is to begin by determining how many pennies would be needed to
# pay the total. Then compute the remainder when this number of pennies is divided
# by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
# the total up.
#

# set conversion to pennies
PENNIES = 100

# input
amount = input("Inserisci la somma (lascia vuoto per uscire) : ")
if amount == "":
    quit()

# set initial amount of total pennies 
tot_amount = 0

# loop to increase pennies
while amount != "":

    # add progressive amount as desire
    tot_amount += float(amount)
    amount = input("Inserisci la somma (lascia vuoto per uscire) : ")

# convert to pennies
tot_pennies = tot_amount * PENNIES

# check if round up or not
round_up = True if tot_pennies % 5 > 2.5 else False

# set how to round up or down
rest = tot_pennies % 5
rounding = 5 - rest if round_up else -rest

# final price
final_price = round((tot_pennies + rounding) / PENNIES, 2)

# print result
print("l'ammonto totale è: %.2f" %tot_amount)
print("Il prezzo finale arrotondato è: %.2f" %final_price)