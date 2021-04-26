##
# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.
#

# user's input
letter = input("Inserisci una lettera dell'alfabeto: ")

# convert letter to lowercase
letter = letter.lower()

# check for vowels
if letter == "a" or letter == "e" \
    or letter == "i" or letter == "o" \
    or letter == "u":
    print("La lettera inserita è una vocale")
# check for y
elif letter == "y":
    print("La lettera inserita è talvolta una vocale, talvolta una consonate")
# check for consonants
else:
    print("La lettera inserita è una consonante") 