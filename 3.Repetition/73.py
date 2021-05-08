##
# One of the first known examples of encryption was used by Julius Caesar. Caesar
# needed to provide written instructions to his generals, but he didn’t want his enemies
# to learn his plans if the message slipped into their hands. As a result, he developed
# what later became known as the Caesar cipher.
# The idea behind this cipher is simple (and as such, it provides no protection against
# modern code breaking techniques). Each letter in the original message is shifted by
# 3 places. As a result, A becomes D, B becomes E, C becomes F, D becomes G, etc.
# The last three letters in the alphabet are wrapped around to the beginning: X becomes
# A, Y becomes B and Z becomes C. Non-letter characters are not modified by the
# cipher.
# Write a program that implements a Caesar cipher. Allow the user to supply the
# message and the shift amount, and then display the shifted message. Ensure that
# your program encodes both uppercase and lowercase letters. Your program should
# also support negative shift values so that it can be used both to encode messages and
# decode messages.

# set limit variable for letters shifting outside number list of unicode characters
ALPH_LIMIT = 26

# user's inputs and set new line variable
line = input("Inserisci un messaggio: ")
shift_amount = int(input("Inserisci il numero di spostamenti (validi anche numeri negativi): "))
new_line = ""

for letter in line:
    # check if is uppercase or lowercase
    is_lower = True if letter.islower() else False
    
    # anyway convert letter to lowercase
    letter = letter.lower()

    # convert to unicode char if it is an alphabet letter
    letter = ord(letter) if letter.isalpha() else letter

    # apply switching 
    if isinstance(letter, int):

        # manage space char: it remains space
        if letter == 32:
            letter = letter
        # limit for "a" unicode char
        elif letter + shift_amount < 97:
            letter = letter + shift_amount + ALPH_LIMIT
        # limit for "z" unicode char
        elif letter + shift_amount > 122:
            letter = letter + shift_amount - ALPH_LIMIT
        else:
            letter = letter + shift_amount

        # convert unicode char to respective
        letter = chr(letter)     
        # make uppercase if initial letter was too
        letter = letter if is_lower else letter.upper()
        # compone new line 
        new_line = new_line + letter

    else:
        new_line = new_line + letter

# print new line
print(new_line)