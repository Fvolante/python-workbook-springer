##
# A particular zoo determines the price of admission based on the age of the guest.
# Guests 2 years of age and less are admitted without charge. Children between 3 and
# 12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
# for all other guests is $23.00.
# Create a program that begins by reading the ages of all of the guests in a group
# from the user, with one age entered on each line. The user will enter a blank line to
# indicate that there are no more guests in the group. Then your program should display
# the admission cost for the group with an appropriate message. The cost should be
# displayed using two decimal places.
#

# set price const
BABY = 0
CHILDREN = 14
SENIORS = 18
ADULTS = 23

# first guest input
guest_age = input("Inserisci l'età del primo visitatore: ")

# set total price variable
tot_price = 0

while guest_age != "":

    # convert to int to compute
    guest_age = int(guest_age)

    # compute price
    if guest_age < 3:
        tot_price += BABY
    elif 3 <= guest_age <= 12:
        tot_price += CHILDREN
    elif 12 < guest_age < 65:
        tot_price += ADULTS
    else:
        tot_price += SENIORS

    guest_age = input("Inserisci l'età del prossimo visitatore (vuoto per terminare): ")   

# print result
print("Il costo totale dei biglietti è %.2f" %tot_price)
