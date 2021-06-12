##
# Using your solutions to Exercises 100 and 102, write a program that generates a
# random good password and displays it. Count and display the number of attempts
# that were needed before a good password was generated. Structure your solution so
# that it imports the functions you wrote previously and then calls them from a function
# named main in the file that you create for this exercise.
#

from es100 import randomPassword
from es102 import validatePassword

def main():

    # set initial number of attempts and first random generate password
    attempt = 1
    password = randomPassword()

    # loop until password is valid and raise attempts number
    while validatePassword(password) == False:
        attempt += 1
        password = randomPassword()

    # results
    print("Tentativi:", attempt)
    print("La password valida è:", password)
    
main()

