##
# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.
#
#    A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
#   because one side of the coin has a loon (a type of bird) on it. The two dollar
#   coin, referred to as a toonie, was introduced 9 years later. It’s name is derived
#   from the combination of the number two and the name of the loonie.
#              

PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25
LOONIE = 100
TOONIE = 200

total = int( input("Inserisci il totale dei cent che vuoi cambiare: ") )

#function to find the rest from a kind of coin
def rest(value, coin):
    return value % coin

#function to find exact value without rest
def total_value(value, coin):
    return value - rest(value, coin)

#function to fin exact amount of a single type of coin
def total_coins(value, coin):
    return int((value - rest(value, coin)) / coin)

#variables to store coins values
toonies_value = total_value(total, TOONIE)
toonies_rest = rest(total, TOONIE)
toonies_coins = total_coins(total, TOONIE)

loonies_value = ( total_value(toonies_rest, LOONIE) )
loonies_rest = rest(toonies_rest, LOONIE)
loonies_coins = total_coins(toonies_rest, LOONIE)

quarter_value = ( total_value(loonies_rest, QUARTER) )
quarter_rest = rest(loonies_rest, QUARTER)
quarter_coins = total_coins(loonies_rest, QUARTER)

quarter_value = ( total_value(loonies_rest, QUARTER) )
quarter_rest = rest(loonies_rest, QUARTER)
quarter_coins = total_coins(loonies_rest, QUARTER)

dime_value = ( total_value(quarter_rest, DIME) )
dime_rest = rest(quarter_rest, DIME)
dime_coins = total_coins(quarter_rest, DIME)

nickel_value = ( total_value(dime_rest, NICKEL) )
nickel_rest = rest(dime_rest, NICKEL)
nickel_coins = total_coins(dime_rest, NICKEL)

penny_value = ( total_value(nickel_rest, PENNY) )
penny_rest = rest(nickel_rest, PENNY)
penny_coins = total_coins(nickel_rest, PENNY) 


#print value exchange
print("Ottieni \n"
        "%i" %toonies_coins, "Toonies, \n" 
        "%i" %loonies_coins, "Loonies, \n"
        "%i" %quarter_coins, "Quarters, \n"
        "%i" %dime_coins, "Dimes, \n"
        "%i" %nickel_coins, "Nickels, \n"
        "%i" %penny_coins, "Pennies,\n",
        "per un totale di: %i" %total)


