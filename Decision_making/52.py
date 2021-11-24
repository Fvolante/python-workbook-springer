##
# At a particular university, letter grades are mapped to grade points in the following
# manner:
#
#   Letter      Grade Points
#   ------------------------
#   A+          4.0
#   A           4.0
#   A-          3.7
#   B+          3.3
#   B           3.0
#   B-          2.7
#   C+          2.3
#   C           2.0
#   C-          1.7
#   D+          1.3
#   D           1.0
#   F           0
#
# Write a program that begins by reading a letter grade from the user. Then your
# program should compute and display the equivalent number of grade points. Ensure
# that your program generates an appropriate error message if the user enters an invalid
# letter grade.
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


# check grade
grade = False

if letter == "A+" or letter == "A":
    grade = A
elif letter == "A-":
    grade = A_MINUS
elif letter == "B+":
    grade = B_PLUS
elif letter == "B":
    grade = B
elif letter == "B-":
    grade = B_MINUS
elif letter == "C+":
    grade = C_PLUS
elif letter == "C":
    grade = C
elif letter == "C-":
    grade = C_MINUS
elif letter == "D+":
    grade = D_PLUS
elif letter == "D":
    grade = D
elif letter == "F":
    grade = F
else:
    print("Il voto inserito non esiste")

# print grade if result exists
if grade:
    print("il voto", letter, "ha un punteggio di:", grade)







