##
# Exercise 52 includes a table that shows the conversion from letter grades to grade
# points at a particular academic institution. In this exercise you will compute the
# grade point average of an arbitrary number of letter grades entered by the user. The
# user will enter a blank line to indicate that all of the grades have been provided. For
# example, if the user enters A, followed by C+, followed by B, followed by a blank
# line then your program should report a grade point average of 3.1.
# You may find your solution to Exercise 52 helpful when completing this exercise.
# Your program does not need to do any error checking. It can assume that each value
# entered by the user will always be a valid letter grade or a blank line.
#

# user's input and conversion to uppercase
letter = input("Inserisci il tuo voto: ")
letter = letter.upper()

# set grade constants
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0

# set variables for grade and counter to compute average
grade = 0
counter = 0

while letter != "":

    counter += 1

    if letter == "A+" or letter == "A":
        grade = grade + A
    elif letter == "A-":
        grade = grade + A_MINUS
    elif letter == "B+":
        grade = grade + B_PLUS
    elif letter == "B":
        grade = grade + B
    elif letter == "B-":
        grade = grade + B_MINUS
    elif letter == "C+":
        grade = grade + C_PLUS
    elif letter == "C":
        grade = grade + C
    elif letter == "C-":
        grade = grade + C_MINUS
    elif letter == "D+":
        grade = grade + D_PLUS
    elif letter == "D":
        grade = grade + D
    elif letter == "F":
        grade = grade + F
    else:
        print("Il voto inserito non esiste")
        # reset last count
        counter -= 1

    # continue looping until blank
    letter = input("Inserisci il tuo voto: ")
    letter = letter.upper()

# compute average
average = grade / counter

# print results
print("Il totale dei voti ha un punteggio di:", grade)
print("La media dei voti è:", average)    