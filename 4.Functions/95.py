##
# Many people do not use capital letters correctly, especially when typing on small
# devices like smart phones. To help address this situation, you will create a function
# that takes a string as its only parameter and returns a new copy of the string that has
# been correctly capitalized. In particular, your function must:
#
#   • Capitalize the first non-space character in the string,
#   • Capitalize the first non-space character after a period, exclamation mark or question
#       mark, and
#   • Capitalize a lowercase “i” if it is preceded by a space and followed by a space,
#       period, exclamation mark, question mark or apostrophe.
#
# Implementing these transformations will correct most capitalization errors. For
# example, if the function is provided with the string “what time do i have to be there?
# what’s the address? this time i’ll try to be on time!” then it should return the string
# “What time do I have to be there? What’s the address? This time I’ll try to be on
# time!”. Include a main program that reads a string from the user, capitalizes it using
# your function, and displays the result.
#

# #
# check if a character is a space
# @param string character
# @return bool
def isSpace(char):
    if char == " ":
        return True
    else:
        return False

# #
# check if a character is a period, an exclamation mark or question mark
# @param string character
# @return bool
def isPerExQuest(char):
    if char == "." or \
        char == "!" or \
        char == "?":
        return True
    else:
        return False  

# #
# check if a character is also an apostrophe 
# @param string character
# @return bool
def isPerExQuestAp(char):
    if char == "'" or \
        char == "." or \
        char == "!" or \
        char == " " or \
        char == "?":
        return True
    else:
        return False


def capitalizedString(string):
    new_string = ""

    for i in range(0, len(string)):
        
        # check if initial characthers are spaces: if not do not insert in new_string
        if i == 0 and isSpace(string[i]):
            pass

        elif isSpace(string[i]) and isSpace(string[i - 1]):
            pass

        else:
            # check capitalize conditions    
            if  isPerExQuest(string[i - 1]):     
                new_string = new_string + string[i].upper()

            elif isPerExQuest(string[i - 2]) and isSpace(string[i - 1]):     
                new_string = new_string + string[i].upper()

            elif string[i] == "i" and \
                isSpace(string[i - 1]) and \
                isPerExQuestAp(string[i + 1]):
                new_string = new_string + string[i].upper()    
            else:
                new_string = new_string + string[i]

    # return capitalized new string   
    return new_string[0].capitalize() + new_string[1:]


print(capitalizedString("what time do i have to be there? what’s the address? this time i’ll try to be on time!"))






