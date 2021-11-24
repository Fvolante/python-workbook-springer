##
# A particular retailer is having a 60 percent off sale on a variety of discontinued
# products. The retailer would like to help its customers determine the reduced price
# of the merchandise by having a printed discount table on the shelf that shows the
# original prices and the prices after the discount has been applied. Write a program that
# uses a loop to generate this table, showing the original price, the discount amount,
# and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
# that the discount amounts and the new prices are rounded to 2 decimal places when
# they are displayed.
#

# set discount rate
DISCOUNT_RATE = 0.60

for i in range(4, 29, 5):

    # compute initial price
    original_price = i + 0.95

    # compute discount
    discount = round(original_price * DISCOUNT_RATE, 2)

    # compute discounted price
    dis_price = round(original_price - discount, 2)

    # print result
    print("Il prezzo iniziale è:", original_price, "$")
    print("Lo sconto applicato del 60% è pari a:", discount, "$")
    print("Il prezzo finale è:", dis_price, "$")
    print("")


   