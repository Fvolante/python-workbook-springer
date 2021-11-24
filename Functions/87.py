##
# An online retailer provides express shipping for many of its items at a rate of $10.95
# for the first item in an order, and $2.95 for each subsequent item in the same order.
# Write a function that takes the number of items in the order as its only parameter.
# Return the shipping charge for the order as the function’s result. Include a main
# program that reads the number of items purchased from the user and displays the
# shipping charge.
#

# set constants prices
FIRST_PRICE = 10.95
EXTRA_PRICE = 2.95

def calc_shipping(items_num):
    #final_price = 0
    if items_num == 1:
        final_price = FIRST_PRICE
    else:
        final_price = FIRST_PRICE + (EXTRA_PRICE * (items_num - 1))
    
    return final_price

def main():
    # items input
    items_num = int(input("Inserisci il numero di prodotti: "))

    print("Il costo totale di spedizione è: %.2f" %calc_shipping(items_num))

if __name__ == "__main__":
    main()
