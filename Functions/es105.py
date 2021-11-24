##
# Write a program that allows the user to convert a number from one base to another.
# Your program should support bases between 2 and 16 for both the input number and
# the result number. If the user chooses a base outside of this range then an appropriate
# error message should be displayed and the program should exit. Divide your program
# into several functions, including a function that converts from an arbitrary base to
# base 10, a function that converts from base 10 to an arbitrary base, and a main
# program that reads the bases and input number from the user. You may find your
# solutions to Exercises 81, 82 and 104 helpful when completing this exercise.
#

# #
# convert decimal number to another base
# @param int number to convert
# @param base number to convert
# @return string new number in selected base
def decToBase(n, end_base):

    # set initial variables, result and rest
    result = ""
    r = 0

    while n != 0:

        r = n % end_base

        # add to final result using letters (if needed) or digits
        if r == 10:
            result = "A" + result
        elif r == 11:
            result = "B" + result
        elif r == 12:
            result = "C" + result
        elif r == 13:
            result = "D" + result
        elif r == 14:
            result = "E" + result
        elif r == 15:
            result = "F" + result
        else:
            result = str(r) + result

        n = n // end_base

    return result

# #
# convert number in given base to decimal
# @param string number to convert
# @param int number base 
# @return int in decimal base
def NumInBaseToDec(n, base):

    # convert n to string to loop on
    n = str(n)

    # set initial decimal conversion
    result = 0

    # set final exponent to compute and loop
    exponent = len(n) - 1

    for digit in n:

        # convert to int to compute
        if digit == "A":
            digit = 10
        elif digit == "B":
            digit = 11
        elif digit == "C":
            digit = 12
        elif digit == "D":
            digit = 13
        elif digit == "E":
            digit = 14
        elif digit == "F":
            digit = 15
        else:
            digit = int(digit)

        # compute conversion of current digit to int
        digit  = digit * (base ** exponent)

        # add int to final int number
        result = result + digit

        # reduce exponent for next looping step
        exponent = exponent - 1

    return result

def main():
    n = input("Inserisci il numero da covertire: ")
    base = int(input("Inserisci la base di partenza del numero da convertire (tra base 2 e base 16): "))
    end_base = int(input("Inserisci la base in cui convertire il numero (tra base 2 e base 16): "))

    if base < 2 or base > 16:
        print("La base di partenza non è valida")
        quit()
    elif end_base < 2 or end_base > 16:
        print("La base finale non è valida")
        quit()

    # control structure to check if n syntax is valid for corresponding base
    if base <= 10:

        for digit in n:
            if int(digit) >= base:
                print("Il numero inserito per questa base non è corretto")
                quit()

    else:

        base_counter = base - 11
        min_char = 65 
        max_char = 65 + base_counter

        for digit in n:
            if digit.isalpha() and  \
                ( ord(digit) < min_char or ord(digit) > max_char):
                print("Il numero inserito per questa base non è corretto")
                quit()

    # execute conversion
    result = NumInBaseToDec(n, base)
    result = decToBase(result, end_base)

    # print result
    print("Il numero:", n, "in base:", base)
    print("Corrisponde a:", result, "in base:", end_base)

main()