##
# Write a program that converts a decimal (base 10) number to binary (base 2). Read the
# decimal number from the user as an integer and then use the division algorithm shown
# below to perform the conversion. When the algorithm completes, result contains the
# binary representation of the number. Display the result, along with an appropriate
# message.
#
# Let result be an empty string
# Let q represent the number to convert
# repeat
# Set r equal to the remainder when q is divided by 2
# Convert r to a string and add it to the beginning of result
# Divide q by 2, discarding any remainder, and store the result back into q
# until q is 0
#

# decimal input
initial_q = int(input("Inserisci un numero intero decimale: "))

# set result variable and r variable for computing
q = initial_q
result = ""
r = 0

# looping using algorithm
while q != 0:

    r = q % 2
    # add to final result
    result = str(r) + result
    q = q // 2

# print result
print("Il numero decimale",initial_q, "corrisponde al binario:", result)
