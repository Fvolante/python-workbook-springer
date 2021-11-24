## 
# In order to win the top prize in a particular lottery, one must match all 6 numbers
# on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
# organizer. Write a program that generates a random selection of 6 numbers for a
# lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
# Display the numbers in ascending order.

from random import randint

""" 
create random group of 6 numbers between 1 and 49. No duplicates
@param: none
@return: list of numbers, in asc order
 """
def ticket_generator():

    #set final list
    ticket = []

    # generate numbers until 6 unique numbers are generated
    while len(ticket) < 6:

        number = randint(1, 49)

        # add to list if unique
        if number not in ticket:
            ticket.append(number)

    # set asc order and return
    return sorted(ticket)

print(ticket_generator())
