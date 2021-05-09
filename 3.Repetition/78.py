##
# Consider a sequence of integers that is constructed in the following manner:
#
# Start with any positive integer as the only term in the sequence
# While the last term in the sequence is not equal to 1 do
# If the last term is even then
# Add another term to the sequence by dividing the last term by 2 using
# floor division
# Else
# Add another term to the sequence by multiplying the last term by 3 and
# adding 1
#
# The Collatz conjecture states that this sequence will eventually end with one when
# it begins with any positive integer. Although this conjecture has never been proved,
# it appears to be true.
# Create a program that reads an integer, n, from the user and reports all of the
# values in the sequence starting with n and ending with one. Your program should
# allow the user to continue entering new n values (and your program should continue
# displaying the sequences) until the user enters a value for n that is less than or equal
# to zero.

# user's input
n = int(input("Inserisci un intero positivo (inserisci 0 o meno per terminare): "))

while n > 1:

    # if not 0 or less is insert print sequence
    while n > 1:

        if n % 2 == 0:
            n = n / 2
            print(int(n))
           
        else:
            n = n * 3 + 1
            print(int(n))
           
    # loop until 0 or less is insert
    n = int(input("Inserisci un intero positivo (inserisci 0 o meno per terminare): "))