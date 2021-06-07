##
# A prime number is an integer greater than one that is only divisible by one and itself.
# Write a function that determines whether or not its parameter is prime, returning
# True if it is, and False otherwise. Write a main program that reads an integer
# from the user and displays a message indicating whether or not it is prime. Ensure
# that the main program will not run if the file containing your solution is imported
# into another program.
#

# #
# check if a number is prime
# @param int
# @bool 

def isPrime(n):
    # set divider not 1 and number itself
    divider = 2

    while divider < n:

        x = n / divider
        
        # immediatly return false if there is any number which n is divisible for
        if x.is_integer():
            return False

        divider += 1

    # exclude 1 and 2 and return 
    if n <= 2:
        return False
    else:
        return True

# main program
def main():
    n = int(input("Inserisci un numero intero: "))

    if isPrime(n):
        print(n, "è un numero primo")
    else:
        print(n, "non è un numero primo")

if __name__ == "__main__":
    main()
