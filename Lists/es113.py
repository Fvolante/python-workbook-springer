## 
# In this exercise, you will create a program that reads words from the user until the
# user enters a blank line. After the user enters a blank line your program should display
# each word entered by the user exactly once. The words should be displayed in
# the same order that they were first entered. 

# set initial list of words
words = []

# user's input until blank line
word = input("Inserisci una parola. Lascia vuoto per terminare:")

while word != "":

    # check presence in list and eventually add word to it
    if word not in words:
        words.append(word)
    
    word = input("Inserisci una parola. Lascia vuoto per terminare:")

# display words in order
for word in words:
    print(word)