##
# In this exercise you will create a function named nextPrime that finds and returns
# the first prime number larger than some integer, n. The value of n will be passed to
# the function as its only parameter. Include a main program that reads an integer from
# the user and displays the first prime number larger than the entered value. Import
# and use your solution to Exercise 98 while completing this exercise.
#

from es98 import isPrime

# #
# return first prime number after the parameter one
# @param integer
# @return next prime number
def nextPrime(n):

    # set next number to parameter and increase it until find prime
    next = n + 1

    while isPrime(next) == False:
        next += 1

    return next

# main program
def main():
    n = int(input("Inserisci un numero intero: "))

    print("Il numero primo successivo a", n, "è:", nextPrime(n))

main()
