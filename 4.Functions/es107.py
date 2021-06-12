##
# Write a function that takes two positive integers that represent the numerator and
# denominator of a fraction as its only parameters. The body of the function should
# reduce the fraction to lowest terms and then return both the numerator and denominator
# of the reduced fraction as its result. For example, if the parameters passed
# to the function are 6 and 63 then the function should return 2 and 21. Include a
# main program that allows the user to enter a numerator and denominator. Then your
# program should display the reduced fraction.
#
#   Hint: In Exercise 79 you wrote a program for computing the greatest common
#   divisor of two positive integers. You may find that code useful when completing
#   this exercise
#

#######
# find greatest common divisor
# @params two positive integers
# @return int MCD

def MCD(n, m):

    # set d to smaller
    d = min(n, m)

    # looping 
    while n % d != 0 or m % d != 0:
        d = d - 1

    return d

#######
# reduce to lowest terms
# @params two positive int

def reduceToLowerTerms(numerator, denominator):

    # find parameters' MCD
    mcd = MCD(numerator, denominator)
    
    return (numerator // mcd, denominator // mcd)

######
# run main program

def main():
    numerator = int(input("Inserisci il numeratore: "))
    denominator = int(input("Inserisci il denominatore: "))

    print("La frazione ridotta ai minimi termini è: %d/%d" %(reduceToLowerTerms(numerator, denominator)))

main()
