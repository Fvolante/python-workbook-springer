##
# When analysing data collected as part of a science experiment it may be desirable
# to remove the most extreme values before performing other calculations. Write a
# function that takes a list of values and an non-negative integer, n, as its parameters.
# The function should create a new copy of the list with the n largest elements and the
# n smallest elements removed. Then it should return the new copy of the list as the
# function’s only result. The order of the elements in the returned list does not have to
# match the order of the elements in the original list.
# Write a main program that demonstrates your function. It should read a list of
# numbers from the user and remove the two largest and two smallest values from it by
# calling the function described previously. Display the list with the outliers removed,
# followed by the original list. Your program should generate an appropriate error
# message if the user enters less than 4 values.
#

""" 
remove smallest and greatest n elements from list
@params: list and non-negative int
@return: new manipulated sorted list
"""
def remove_largest (values, n):

    # create sorted copy of param list
    values = sorted(values)

    # splice n elements from list and return
    return values[n:-n]

def main():

    # set initial list
    values = []

    # user's inputs until 0 is typed
    value = float(input("Inserisci un numero:"))

    while value != 0.0:

        # append rounded value to list
        values.append(round(value, 2))

        value = float(input("Inserisci un numero. Inserisci untotale di almeno 4 valori. 0 per uscire:"))


    # display error message for short list or display correct lists
    if len(values) < 4:
        print("I valori inseriti sono meno di 4")
        exit()
    else:
        print("La nuova lista è:", remove_largest(values, 2))
        print("La lista originale è:", values)

main()




    