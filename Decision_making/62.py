##
# A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
# are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
# 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
# between 1 and 36 are used to number the black spaces.
# Many different bets can be placed in roulette.We will only consider the following
# subset of them in this exercise:
#
# • Single number (1 to 36, 0, or 00)
# • Red versus Black
# • Odd versus Even (Note that 0 and 00 do not pay out for even)
# • 1 to 18 versus 19 to 36
#
# Write a program that simulates a spin of a roulette wheel by using Python’s
# random number generator. Display the number that was selected and all of the bets
# that must be payed. For example, if 13 is selected then your program should display:
#
# The spin resulted in 13...
# Pay 13
# Pay Black
# Pay Odd
# Pay 1 to 18
#
# If the simulation results in 0 or 00 then your program should display Pay 0
# or Pay 00 without any further output.
#
import random

# generate random number. Create strings for 00 and 0
number = random.randint(0,37)
number = "00" if number == 37 else number
number = "0" if number == 0 else number

################
# Define prizes
#

# Single number
SINGLE = number

# Red vs Black
if number == 1 or \
    number == 3  or \
    number == 5  or \
    number == 7  or \
    number == 9  or \
    number == 12 or \
    number == 14 or \
    number == 16 or \
    number == 18 or \
    number == 19 or \
    number == 21 or \
    number == 23 or \
    number == 25 or \
    number == 27 or \
    number == 30 or \
    number == 32 or \
    number == 34 or \
    number == 36:
    COLOR = "Rosso"
else:
    COLOR = "Nero"

# Even or Odd
if isinstance(number, int):
    if number % 2 == 0:
        EVEN_ODD = "Pari"
    else:
        EVEN_ODD = "Dispari"

# first or second half
if isinstance(number, int):
    if 1 < number <= 18:
        HALF = "da 1 a 18"
    else:
        HALF = "da 19 a 38"

# display results
print("Il giro di roulette pesca il %s..." %number)

if number == "0" or number == "00":
    print("Paga il", SINGLE)
else:
    print("Paga il", SINGLE)
    print("Paga il", COLOR)
    print("Paga il", EVEN_ODD)
    print("Paga la metà", HALF)