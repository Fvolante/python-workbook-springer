##
# In the previous exercise you created a program that converted a letter grade into the
# equivalent number of grade points. In this exercise you will create a program that
# reverses the process and converts from a grade point value entered by the user to a
# letter grade. Ensure that your program handles grade point values that fall between
# letter grades. These should be rounded to the closest letter grade. Your program
# should report A+ if the value entered by the user is 4.0 or more.
#

# set grade constants
A_PLUS = 4.0
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

# user's points
points = float(input("Inserisci il punteggio: "))

# function to find differrences from closest constants
def find_diff (higher, lower, points):
    diff_up = abs(higher - points)
    diff_down = abs(lower - points)
    diff_min = min(diff_up, diff_down)
    
    if diff_min == diff_up:
        return higher
    else:
        return lower

# check votes:
if A_PLUS >= points >= A_MINUS:
    if find_diff(A_PLUS, A_MINUS, points) == A_PLUS:
       vote = "A+"
    else:
        vote = "A-"


elif A_MINUS >= points >= B_PLUS:
    if find_diff(A_MINUS, B_PLUS, points) == A_MINUS:
       vote = "A-"
    else:
        vote = "B+"

elif B_PLUS >= points >= B:
    if find_diff(B_PLUS, B, points) == B_PLUS:
       vote = "B+"
    else:
        vote = "B"

elif B >= points >= B_MINUS:
    if find_diff(B, B_MINUS, points) == B:
       vote = "B"
    else:
        vote = "B-"

elif B_MINUS >= points >= C_PLUS:
    if find_diff(B_MINUS, C_PLUS, points) == B_MINUS:
       vote = "B-"
    else:
        vote = "C+"

elif C_PLUS >= points >= C:
    if find_diff(C_PLUS, C, points) == C_PLUS:
       vote = "C+"
    else:
        vote = "C"

elif C >= points >= C_MINUS:
    if find_diff(C, C_MINUS, points) == C:
       vote = "C"
    else:
        vote = "C-"

elif C_MINUS >= points >= D_PLUS:
    if find_diff(C_MINUS, D_PLUS, points) == C_MINUS:
       vote = "C-"
    else:
        vote = "D+"

elif D_PLUS >= points >= D:
    if find_diff(D_PLUS, D, points) == D_PLUS:
       vote = "D+"
    else:
        vote = "D"

elif D >= points >= F:
    if find_diff(D, F, points) == D:
       vote = "D"
    else:
        vote = "F"

# print result
print("Il punteggio", points, "corrisponde al voto", vote)


   




