##
# In a particular jurisdiction, older license plates consist of three uppercase letters
# followed by three digits. When all of the license plates following that pattern had
# been used, the format was changed to four digits followed by three uppercase letters.
# Write a program that begins by reading a string of characters from the user. Then
# your program should display a message indicating whether the characters are valid
# for an older style license plate or a newer style license plate. Your program should
# display an appropriate message if the string entered by the user is not valid for either
# style of license plate.
#

# input
plate = input("Inserisci il numero di targa: ")

error = False

# check errors on str lenght and uppercase inputs
if len(plate) != 6 and len(plate) != 7:
    error = True 
elif plate.isupper() == False:
    error = True

# check 6 char cases
if len(plate) == 6:
    if plate[:3].isalpha() and plate[3:].isnumeric():
        plate_format = "old"
    else:
        error = True

# check 7 char cases
elif len(plate) == 7:  
    if plate[:4].isnumeric() and plate[4:].isalpha():
        plate_format = "new"
    else:
        error = True

# print result
if error:
    print("Il formato di targa inserito non è valido")
elif plate_format == "old":
    print("Il formato di targa è quello vecchio")
elif plate_format == "new":
    print("Il formato di targa è quello nuovo")

