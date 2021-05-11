##
# Write a function that takes the lengths of the two shorter sides of a right triangle as
# its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
# theorem, as the function’s result. Include a main program that reads the lengths of
# the shorter sides of a right triangle from the user, uses your function to compute the
# length of the hypotenuse, and displays the result.
#

# import function from file import_85
from import_85 import hypotenuse

# define main function for control structure
def main():
    # cathetuses
    a = float(input("Inserisci il primo cateto del quadrato: "))
    b = float(input("Inserisci il secondo cateto del quadrato: "))

    # print result
    print("L'ipotenusa del triangolo è:", hypotenuse(a, b))

# control structure
if __name__ == "__main__":
    main()
