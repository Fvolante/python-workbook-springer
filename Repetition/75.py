##
# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromic words. Write a program
# that reads a string from the user and uses a loop to determine whether or not it is a
# palindrome. Display the result, including a meaningful output message.

# input and new variable
word = input("Inserisci una parola: ")
pal_word = ""


for letter in word:
    # add letter in reverse way
    pal_word = letter + pal_word

# create a condition for result message
is_pal = True if word == pal_word else False

# print appropiate result messages
if is_pal:
    print("La parola", word, "è palindroma")
else:
    print("La parola", word, "non è palindroma")
    print("il suo inverso è", pal_word)



""" QUICK WAY:

word = "anna"
palindrome = word[::-1]

if word == palindrome:
    print("La parola", word, "è palindroma")
else:
    print("La parola", word, "non è palindroma")
    print("il suo inverso è", palindrome) """

