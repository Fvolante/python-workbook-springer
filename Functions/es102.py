##
# In this exercise you will write a function that determines whether or not a password
# is good.We will define a good password to be a one that is at least 8 characters long
# and contains at least one uppercase letter, at least one lowercase letter, and at least
# one number. Your function should return True if the password passed to it as its
# only parameter is good. Otherwise it should return False. Include a main program
# that reads a password from the user and reports whether or not it is good. Ensure
# that your main program only runs when your solution has not been imported into
# another file.

# #
# validate password
# @param string as password
# @return bool

def validatePassword(password):

    # set initial validation variables as false
    lower = False
    upper = False
    digits = False
    length = False

    # check at least 8 character lenght
    if len(password) >= 8:
        length = True

    # loop on password to check others requirements
    for i in range(0, len(password)):
        
        # at least one lowercase char
        if password[i].islower():
            lower = True

        # at least one uppercase char
        if password[i].isupper():
            upper = True

        # at least one digit char
        if password[i].isdigit():
            digits = True

    # result
    if lower and length and upper and digits:
        return True
    else:
        return False

# set and execute main program
def main():
    password = input("Inserisci una password: ")

    if validatePassword(password):
        print("Password valida")
    else:
        print("Password non valida")

if __name__ == "__main__":
    main()