##
# There are numerous phrases that are palindromes when spacing is ignored. Examples
# include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
# among many others. Extend your solution to Exercise 75 so that it ignores spacing
# while determining whether or not a string is a palindrome. For an additional challenge,
# further extend your solution so that is also ignores punctuation marks and treats
# uppercase and lowercase letters as equivalent.
#

# input
line = input("Inserisci una frase: ")

# set two comparison lines
origin_line = ""
new_line = ""

# looping and create two comparison lines
for letter in line:
    
    if letter.isalpha():
        origin_line = origin_line + letter
        new_line = letter + new_line

# check palyndrome and print result
if origin_line == new_line:
    print("La frase è palindroma")
else:
    print("La frase non è palidroma")


