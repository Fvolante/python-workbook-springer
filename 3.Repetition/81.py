##
# Write a program that converts a binary (base 2) number to decimal (base 10). Your
# program should begin by reading the binary number from the user as a string. Then
# it should compute the equivalent decimal number by processing each digit in the
# binary number. Finally, your program should display the equivalent decimal number
# with an appropriate message.
#

# binary unber input
bin_num = input("Inserisci un numero binario: ")

# set initial decimal conversion
dec_num = 0

# set final exponent to compute and loop
exponent = len(bin_num) - 1

for digit in bin_num:

    # convert to int to compute
    digit = int(digit)

    # compute conversion of current digit to int
    digit  = digit * (2 ** exponent)

    # add int to final int number
    dec_num = dec_num + digit

    # reduce exponent for next looping step
    exponent = exponent - 1

# print result
print("Il binario", bin_num,"corrisponde a:", dec_num)