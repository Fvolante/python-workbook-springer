##
# Words like first, second and third are referred to as ordinal numbers. In this exercise,
# you will write a function that takes an integer as its only parameter and returns a
# string containing the appropriate English ordinal number as its only result. Your
# function must handle the integers between 1 and 12 (inclusive). It should return an
# empty string if the function is called with an argument outside of this range. Include
# a main program that demonstrates your function by displaying each integer from 1
# to 12 and its ordinal number. Your main program should only run when your file has
# not been imported into another program.
#

# compute conversion
def ordinal(num):

    if num == 1:
        num = "first"
    elif num == 2:
        num = "second"
    elif num == 3:
        num = "third"
    elif num == 4:
        num = "fourth"
    elif num == 5:
        num = "fifth"
    elif num == 6:
        num = "sixth"
    elif num == 7:
        num = "seventh"
    elif num == 8:
        num = "eight"
    elif num == 9:
        num = "ninth"
    elif num == 10:
        num = "tenth"
    elif num == 11:
        num = "eleventh"
    elif num == 12:
        num = "twelfth"
    else:
        num = ""

    return num 

def main():
    for i in range(1, 13):
        print("The ordinal for", i, "is:", ordinal(i))

if __name__ == "__main__":
    main()