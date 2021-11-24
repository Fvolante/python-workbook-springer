## 
# Write a function that determines whether or not a list of values is in sorted order
# (either ascending or descending). The function should return True if the list is
# already sorted. Otherwise it should return False. Write a main program that reads
# a list of numbers from the user and then uses your function to report whether or not
# the list is sorted.
# Make sure you consider these questions when completing this exercise: Is a
# list that is empty in sorted order? What about a list containing one element?

""" 
check if a list of values is sorted in ascending or descending order
@params: a list of values
@return: bool: if list is sorted or not
"""
def is_sorted(values):

    # create sorted list of param
    asc_values = sorted(values)
    desc_values = sorted(values, reverse=True)

    # check equality and return
    if values == asc_values or values == desc_values:
        return True
    else:
        return False

def main():

    values = input("Inserisci un elenco di numeri. Separa ogni numero con uno spazio bianco:\n")

    # convert values inserted by user in list of strings
    values = values.split()

    # convert each value in float number
    values = [float(i) for i in values]

    if is_sorted(values):
        print("L'elenco dei valori è ordinato")

    else:
        print("L'elenco dei valori non è ordinato")

main() 

