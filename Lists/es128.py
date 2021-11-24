## 
# Python’s standard library includes a method named count that determines how
# many times a specific value occurs in a list. In this exercise, you will create a new
# function named countRange. It will determine and return the number of elements
# within a list that are greater than or equal to some minimum value and less than some
# maximum value. Your function will take three parameters: the list, the minimum
# value and the maximum value. It will return an integer result greater than or equal to
# 0. Include a main program that demonstrates your function for several different lists,
# minimum values and maximum values. Ensure that your program works correctly
# for both lists of integers and lists of floating-point numbers.

""" 
count elements in a list that are between a given min and max value
@params: list of valures, int: min count value, int: max count value
@return: int: number of elements in param list in range
"""
def countRange(values, min, max):

    # set final list of values
    count = 0

    for value in values:

        if min <= value < max:

           count += 1

    return count  

def main():

    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print("In una lista tra 1 e 10 i valori compresi tra 5 e 7 sono:")
    print("Risultato: %d" %countRange(values, 5, 7))

    print("In una lista tra 1 e 10 i valori compresi tra 11 e 23 sono:")
    print("Risultato: %d" %countRange(values, 11, 23))

    print("In una lista tra 1 e 10 i valori compresi tra -1 e 15 sono:")
    print("Risultato: %d" %countRange(values, -1, 15))

main()