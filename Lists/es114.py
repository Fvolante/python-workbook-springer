## 
# Create a program that reads integers from the user until a blank line is entered. Once
# all of the integers have been read your program should display all of the negative
# numbers, followed by all of the zeros, followed by all of the positive numbers.Within
# each group the numbers should be displayed in the same order that they were entered
# by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
# your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
# should display each value on its own line.

# set initial lists for neagtive, zeros and positive integers
neg = []
zeros = []
pos = []

# insert values until blank is typed
value = input("Inserisci un numero intero. Lascia vuoto per terminare:")

while value != "":
    
    # convert input to int
    value = int(value)

    # check if value is negative, zero or positive and add to appropriate list
    if value < 0:
        neg.append(value)

    elif value == 0:
        zeros.append(value)
    
    elif value > 0:
        pos.append(value)

    value = input("Inserisci un numero intero. Lascia vuoto per terminare:")

# combine all previous lists in final one
result_list = neg + zeros + pos

# print results in order, one value per line
for number in result_list:
    print(number)