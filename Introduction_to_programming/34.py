##
# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. Each of
# these amounts should be displayed on its own line with an appropriate label. All of
# the values should be displayed using two decimal places, and the decimal points in
# all of the numbers should be aligned when reasonable values are entered by the user.
#

# price regular
REGULAR_PRICE = 3.49
DISCOUNT_PRICE = REGULAR_PRICE * 0.60

# user's input
old_loaves = int(input("Inserisci il numero di pagnotte del giorno prima acquistate: "))

# compute regular price
tot_reg_price = old_loaves * REGULAR_PRICE

# compute total discount
tot_dis_price = old_loaves * DISCOUNT_PRICE

# compute final total price
final_price = tot_reg_price - tot_dis_price

print("Per un totale di", old_loaves, "pagnotte")
print("il prezzo totale senza sconto: %5.2f $" %tot_reg_price)
print("il totale sconto applicato:    %5.2f $" %tot_dis_price)
print("il prezzo finale:              %5.2f $" %final_price)