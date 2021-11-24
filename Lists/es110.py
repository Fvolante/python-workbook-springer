##
# Write a program that reads integers from the user and stores them in a list. Your
# program should continue reading values until the user enters 0. Then it should display
# all of the values entered by the user (except for the 0) in ascending order, with one
# value appearing on each line. Use either the sort method or the sorted function
# to sort the list.
#

# Set initial empty list
values = []

# read user's inputs
value = int(input("inserisci un numero intero. Inserisci '0' per terminare il programma:"))

while value != 0:

    values.append(value)

    value = int(input("inserisci un numero intero. Inserisci '0' per terminare il programma:"))

# order in asc ( sort() method )
values.sort()

# print value one per line
for value in values:
    print(value)


""" 
with sorted funcion:

values = sorted(values)

for value in values:
    print(value)

"""    