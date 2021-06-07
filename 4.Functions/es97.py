##
# Write a function named precedence that returns an integer representing the precedence
# of a mathematical operator. A string containing the operator will be passed to
# the function as its only parameter. Your function should return 1 for + and -, 2 for *
# and /, and 3 for ˆ. If the string passed to the function is not one of these operators
# then the function should return -1. Include a main program that reads an operator
# from the user and either displays the operator’s precedence or an error message indicating
# that the input was not an operator. Your main program should only run when
# the file containing your solution has not been imported into another program.
#
#   In this exercise, along with others that appear later in the book, we will use
#   ˆ to represent exponentiation. Using ˆ instead of Python’s choice of **
#   will make these exercises easier because an operator will always be a single
#   character.
#

# #
# represent math operator precedence
# @param string which is a math operator
# @return int for precedence
def precedence(s):

    if s == "+" or s == "-":
        return 1
    
    elif s == "*" or s == "/":
        return 2

    elif s == "^":
        return 3

    else:
        return -1

# define and launch main program
def main():
    s = input("Inserisci un operatore matematico: ")\
    
    s = precedence(s)

    if s == -1:
        print("Errore: il carattere inserito non è un operatore valido")
    else:
        print("Il carattere inserito ha un valore di precedenza di:", s)

if __name__ == "__main__":
    main()
    