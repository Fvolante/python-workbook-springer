##
# Write two functions, hex2int and int2hex, that convert between hexadecimal
# digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and decimal (base 10) integers.
# The hex2int function is responsible for converting a string containing a single
# hexadecimal digit to a base 10 integer, while the int2hex function is responsible
# for converting an integer between 0 and 15 to a single hexadecimal digit. Each
# function will take the value to convert as its only parameter and return the converted
# value as its only result. Ensure that the hex2int function works correctly for both
# uppercase and lowercase letters. Your functions should display a meaningful error
# message and end the program if the parameter’s value is outside of the expected
# range.
#

# #
# convert hexadecimal letter to decimal integers
# @param string hexadecimal letter
# @return converted decimal int or display error message
def hexLetters(letter):
    letter = letter.upper()

    if letter == "A":
        letter = 10
    elif letter == "B":
        letter = 11 
    elif letter == "C":
        letter = 12
    elif letter == "D":
        letter = 13
    elif letter == "E":
        letter = 14
    elif letter == "F":
        letter = 15
    else:
        print("Valore inserito non valido")
        return

    return letter    

# #
# convert hexadecimal number to decimal
# @param string valid hexadecimal
# @return converted decimal int 
def hex2int(n):
    # set initial exponent to make conversion and converted inital decimal number
    exponent = len(n) - 1
    result = 0

    # loop on parameter
    for char in n:

        # manage if character is a number
        if char.isdigit():
            char = int(char) * (16 ** exponent)
            result = result + char

        # manage if character is a hex letter
        else:

            if "A" < char.upper() < "F":
                char = hexLetters(char) * (16 ** exponent)
                result = result + char

            else:
                print("Il valore inserito non è valido")
                return
        exponent -= 1

    return result

# #
# convert decimal int between 0 and 15 to hexadecimal
# @param int between 0 and 15
# @return string hexadecimal
def int2hex(n):

    n = int(n)

    if n < 0 or n > 15:
        print("Il numero inserito è errato")
        return

    if 0 <= n <= 9:
        n = str(n)

    else:

        if n == 10:
            n = "A"

        elif n == 11:
            n = "B"

        elif n == 12:
            n = "C"

        elif n == 13:
            n = "D"

        elif n == 14:
            n = "E"

        elif n == 15:
            n = "F"

    return n

