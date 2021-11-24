##
# Write a program that reads integers from the user and stores them in a list. Use 0 as
# a sentinel value to mark the end of the input. Once all of the values have been read
# your program should display them (except for the 0) in reverse order, with one value
# appearing on each line.
#

# Set initial empty list
values = []

# read input from user and store them in list
value = int(input("inserisci un numero intero (digita \"0\" per uscire): "))

while value != 0:

    values.append(value)

    value = int(input("inserisci un numero intero (digita \"0\" per uscire): "))

# reverse order of values
values.reverse()

# print values one per line
for value in values:
    print(value)