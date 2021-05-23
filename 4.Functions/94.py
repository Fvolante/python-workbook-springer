##
# If you have 3 straws, possibly of differing lengths, it may or may not be possible
#to lay them down so that they form a triangle when their ends are touching. For
# example, if all of the straws have a length of 6 inches then one can easily construct
# an equilateral triangle using them. However, if one straw is 6 inches long, while
# the other two are each only 2 inches long, then a triangle cannot be formed. More
# generally, if any one length is greater than or equal to the sum of the other two then
# the lengths cannot be used to form a triangle. Otherwise they can form a triangle.
# Write a function that determines whether or not three lengths can form a triangle.
# The function will take 3 parameters and return a Boolean result. If any of the lengths
# are less than or equal to 0 then your function should return False. Otherwise it
# should determine whether or not the lengths can be used to form a triangle using
# the method described in the previous paragraph, and return the appropriate result.
# In addition, write a program that reads 3 lengths from the user and demonstrates the
# behaviour of your function.
#

# #
# @params float side of triangle
# @return bool
#

def isTriangle(a, b, c):

    # check if any side is less than 0
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # check triangle 
    if a >= b + c or \
        b >= a + c or \
        c >= a + b:
        return False
    else:
        return True

def main():
    a = float(input("Inserisci la misura del lato a: "))
    b = float(input("Inserisci la misura del lato b: "))
    c = float(input("Inserisci la misura del lato c: "))

    if isTriangle(a, b, c):
        print("Le misure sono valide per formare un triangolo")
    else:
        print("Le misure non sono valide per formare un triangolo")

main()    