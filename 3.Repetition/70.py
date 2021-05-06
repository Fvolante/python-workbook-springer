##
# A parity bit is a simple mechanism for detecting errors in data transmitted over an
# unreliable connection such as a telephone line. The basic idea is that an additional bit
# is transmitted after each group of 8 bits so that a single bit error in the transmission
# can be detected.
# Parity bits can be computed for either even parity or odd parity. If even parity
# is selected then the parity bit that is transmitted is chosen so that the total number
# of one bits transmitted (8 bits of data plus the parity bit) is even. When odd parity
# is selected the parity bit is chosen so that the total number of one bits transmitted
# is odd.
# Write a program that computes the parity bit for groups of 8 bits entered by the
# user using even parity. Your program should read strings containing 8 bits until the
# user enters a blank line. After each string is entered by the user your program should
# display a clear message indicating whether the parity bit should be 0 or 1. Display
# an appropriate error message if the user enters something other than 8 bits.
#
#   Hint: You should read the input from the user as a string. Then you can use
#   the count method to help you determine the number of zeros and ones in the
#   string. Information about the count method is available online.
#

# input line
bit_group = input("Inserisci un gruppo di 8 bit (vuoto per terminare): ")

while bit_group != "":

    # count 0 and 1 occurrencies
    count_0 = bit_group.count("0")
    count_1 = bit_group.count("1")

    # set error if bit_group is wrong
    digit_error = True if count_0 + count_1 != 8 else False

    if digit_error:
        # display error message 
        print("Stringa inserita errata")
        print("Hai inserito:", bit_group)
        print("")
    else:
        is_even = True if int(bit_group, 2) % 2 == 0 else False
        parity_bit = "0" if is_even else "1"

        print("Il binario:", bit_group,"è:", int(bit_group, 2))
        insert_bit = input("Inserisci il bit di parità: " + parity_bit + ": ")

        # if wrong parity bit inserted print error message
        if insert_bit != parity_bit:
            print("Il Parity bit inserito è errato")

    # new input required
    bit_group = input("Inserisci un gruppo di 8 bit (vuoto per terminare): ")