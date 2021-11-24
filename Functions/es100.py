##
# Write a function that generates a random password. The password should have a
# random length of between 7 and 10 characters. Each character should be randomly
# selected from positions 33 to 126 in the ASCII table. Your function will not take
# any parameters. It will return the randomly generated password as its only result.
# Display the randomly generated password in your file’s main program. Your main
# program should only run when your solution has not been imported into another file.
#
#   Hint: You will probably find the chr function helpful when completing this
#   exercise. Detailed information about this function is available online.
#

from random import randint

# #
# generate random password with random lenght of between 7 and 10 ASCII character (from positions 33 to 126)
# @return 

def randomPassword():

    # set initial password as empty string 
    password = ""

    # set password lenght
    length = randint(7, 10)
  
    # add to password unicode char for lenght value
    for i in range(length):
        value = str( chr(randint(33, 126)) )

        password = password + value

    return password

# set and run main program
def main():
    print(randomPassword())

if __name__ == "__main__":
    main()
    




