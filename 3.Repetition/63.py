##
# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
#
#   Hint: Because the 0 marks the end of the input it should not be included in the
#   average.
#

# set inputs and starting variables
value = float(input("Inserisci un numero: "))
# set counter to compute average
i = 0
# set initial sum of values
values_sum = 0
    
# insert values until 0 is insert    
while value != 0:
    i += 1
    values_sum = values_sum + value

    # insert new value
    value = float(input("Inserisci un numero (0 per uscire): "))

# compute average
average = round(values_sum / i, 2)

# print results
if values_sum != 0:
    print("La media dei valori inseriti è", average)
else:
    print("Il valore inserito non è corretto")