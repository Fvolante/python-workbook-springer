## 
# Write a program that reads numbers from the user until a blank line is entered. Your
# program should display the average of all of the values entered by the user. Then
# the program should display all of the below average values, followed by all of the
# average values (if any), followed by all of the above average values. An appropriate
# label should be displayed before each list of values.

""" 
return average of inserted values
@param: a list of numeric values
@return: a number, average rounded to 2 decimals
 """
def average(values):

    return round(sum(values) / len(values), 2)

# main program
def main():

    # set list for values
    values = []

    # insert value from user
    value = input("inserisci un numero. Lascia vuoto per uscire:\n")

    while value != "":

        #convert to float number and append to list, then loop
        value = float(value)

        values.append(value)

        value = input("inserisci un numero. Lascia vuoto per uscire:\n")

    # check if no values are inserted and exit
    if bool(values) == False:
        print("Nessun valore inserito")
        exit()

    # set average in variable, and lists of values in relationship to av by list comprehensions
    av = float(average(values))
    under_av = [ i for i in values if i < av ]
    exact_av = [ i for i in values if i == av ]  
    top_av = [ i for i in values if i > av ]
    
    # print values
    print("La media dei valori inseriti è:\n", av)

    print("I valori sotto la media sono:")
    print(under_av)
    
    if bool(exact_av) == True:
        print("I valori di media esatta sono:")
        print(exact_av)

    print("I valori sopra la media sono:")
    print(top_av)

main()