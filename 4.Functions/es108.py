##
# Many recipe books still use cups, tablespoons and teaspoons to describe the volumes
# of ingredients used when cooking or baking. While such recipes are easy enough to
# follow if you have the appropriate measuring cups and spoons, they can be difficult
# to double, triple or quadruple when cooking Christmas dinner for the entire extended
# family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16
# tablespoons when quadrupled. However, 16 tablespoons would be better expressed
# (and easier to measure) as 1 cup.
# Write a function that expresses an imperial volume using the largest units possible.
# The function will take the number of units as its first parameter, and the unit
# of measure (cup, tablespoon or teaspoon) as its second parameter. It will return a
# string representing the measure using the largest possible units as its only result. For
# example, if the function is provided with parameters representing 59 teaspoons then
# it should return the string “1 cup, 3 tablespoons, 2 teaspoons”.
#
#   Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent
#   to 3 teaspoons.
#

def convertUnits(units, measure):

    # set base units of measure
    TEASPOON = 1
    TABLESPOON = 3 * TEASPOON
    CUP = 16 * TABLESPOON
  
    # convert every inserted measure to teaspoon
    if measure == "teaspoon":
        units = units
    elif measure == "tablespoon":
        units = units * TABLESPOON
    elif measure == "cup":
        units = units * CUP

    # compute final conversion
    rest_cups = units % CUP
    cups = units // CUP
    tablespoons = rest_cups // TABLESPOON
    teaspoons = rest_cups % TABLESPOON

    # compone result string
    result = ""
    
    if cups == 1:
        result = result + "1 cup"
    elif cups > 1:
        result = result + str(cups) + " cups"
    else:
        result = result

    if bool(cups) == True and (bool(tablespoons) == True or bool(teaspoons)):
        result = result + ", "

    if tablespoons == 1:
        result = result + "1 tablespoon"
    elif tablespoons > 1:
        result = result + str(tablespoons) + " tablespoons"
    else:
        result = result

    if bool(tablespoons) == True and bool(teaspoons):
        result = result + ", "
    
    if teaspoons == 1:
        result = result + "1 teaspoon"
    elif teaspoons > 1:
        result = result + str(teaspoons) + " teaspoons"
    else:
        result = result

    return result

def main():
    print("59 teaspoons:", convertUnits(59, "teaspoon"))
    print("49 teaspoons:", convertUnits(49, "teaspoon"))
    print("66 teaspoons:", convertUnits(66, "teaspoon"))
    print("560 teaspoons:", convertUnits(560, "teaspoon"))
    print("50 tablespoon:", convertUnits(50, "tablespoon"))
    print("21 tablespoon:", convertUnits(21, "tablespoon"))
    print("16 tablespoon:", convertUnits(16, "tablespoon"))
    print("54 tablespoon:", convertUnits(54, "tablespoon"))

main()