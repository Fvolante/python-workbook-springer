##
# In a particular jurisdiction, older license plates consist of three letters followed by
# three digits. When all of the license plates following that pattern had been used, the
# format was changed to four digits followed by three letters.
# Write a function that generates a random license plate. Your function should have
# approximately equal odds of generating a sequence of characters for an old license
# plate or a new license plate. Write a main program that calls your function and
# displays the randomly generated license plate.
#

from random import randint, choice
from string import ascii_letters, digits

def generatePlate():

    # set initial plate as ampty string
    plate = ""

    # generate old or new format: 0 for old, 1 for new one
    format = randint(0, 1)

    # generate random numbers and letters and compone plate
    # old format:
    if format == 0:
        for i in range(3):
            plate = plate + choice(ascii_letters)

        for i in range(3):
            plate = plate + choice(digits)

    # new format:
    else:
        for i in range(4):
            plate = plate + choice(digits)

        for i in range(3):
            plate = plate + choice(ascii_letters)

    return plate


def main():
    print("La tua targa è:", generatePlate())

main()

