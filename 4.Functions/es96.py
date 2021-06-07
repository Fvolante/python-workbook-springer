##
# In this exercise you will write a function named isInteger that determines
# whether or not the characters in a string represent a valid integer. When determining
# if a string represents an integer you should ignore any leading or trailing
# white space. Once this white space is ignored, a string represents an integer if its
# length is at least one and it only contains digits, or if its first character is either +
# or - and the first character is followed by one or more characters, all of which are
# digits.
# Write a main program that reads a string from the user and reports whether or
# not it represents an integer. Ensure that the main program will not run if the file
# containing your solution is imported into another program.
#
#   Hint: You may find the lstrip, rstrip and/or strip methods for strings
#   helpful when completing this exercise. Documentation for these methods is
#   available online.
#   Exercise
#

# # #
# check if a string is a valid integer
# @param sting
# #return bool
#

def isInteger(s):
    # remove white spaces from string
    s = s.strip()

    # chek if first char is "+" or "-" and others are numbers
    if (s[0] == "+" or s[0] == "-") and \
        s[1:].isnumeric():
        
        return True
    
    # check if all char are numbers
    elif s.isnumeric():
        return True

    else:
        return False

def main():
    s = input("Inserisci la stringa: ")
    
    if isInteger(s):
        print("La stringa è un numero intero")
    else:
        print("La stringa non è un numero intero")


if __name__ == "__main__":
    main()









