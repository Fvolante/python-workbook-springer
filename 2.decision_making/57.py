##
# A particular cell phone plan includes 50 minutes of air time and 50 text messages
# for $15.00 a month. Each additional minute of air time costs $0.25, while additional
# text messages cost $0.15 each. All cell phone bills include an additional charge of
# $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
# subject to 5 percent sales tax.
# Write a program that reads the number of minutes and text messages used in a
# month from the user. Display the base charge, additional minutes charge (if any),
# additional text message charge (if any), the 911 fee, tax and total bill amount. Only
# display the additional minute and text message charges if the user incurred costs in
# these categories. Ensure that all of the charges are displayed using 2 decimal places.
#

# set charge const
MIN_EXTRA_COST = 0.25
MESS_EXTRA_COST = 0.15
SUPPORT_911 = 0.44

# tax in %
TAX_RATE = 0.05

# user's inputs
minutes = int(input("Inserisci il numero di minuti di chiamate impiegati: "))
messages = int(input("Inserisci il numero di messaggi inviati: "))

# set base charge
base_charge = 15.00 

# find amount of extra minutes and messages if they are more than 50
extra_min = minutes - 50 if minutes > 50 else 0
extra_mess = messages - 50 if messages > 50 else 0

# set the base charge without taxes
if minutes <= 50 and messages <= 50:
    pass

else:
    mess_cost = extra_mess * MESS_EXTRA_COST
    min_cost = extra_min * MIN_EXTRA_COST
    base_charge = base_charge + min_cost + mess_cost

# compute final charge
charge = base_charge + SUPPORT_911
taxes = round(charge * TAX_RATE, 2)
final_charge = round(charge + taxes, 2)
charge_message = "La tua bolletta mensile è equivalente al costo base di", base_charge, "euri più il costo di supporto al 911 di", SUPPORT_911, " euri e il costo di tasse dello 0.5%, pari a", taxes, "euri."

# print result
if base_charge == 15.00:
    print("Non hai superato la soglia massima di minuti e messaggi spesi.")
    print(charge_message)
elif minutes > 50 and messages <= 50:
    print("Hai superato la soglia massima di minuti totali di", extra_min)
    print(charge_message)
elif messages > 50 and minutes <= 50:
    print("Hai superato la soglia massima di messaggi totali di", extra_min)
    print(charge_message)
else:
    print("Hai superato la soglia massima di messaggi totali di", extra_min, "e la soglia massima di minuti totali di", extra_mess)
    print(charge_message)