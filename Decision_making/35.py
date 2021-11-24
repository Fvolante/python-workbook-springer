##
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.
#

# user's input
number = int(input("Inserisci un numero intero: "))

# check even or odd
if number % 2 == 0:
    print("Il numero", number, "è pari")
else:
    print("Il numero", number, "è dispari")