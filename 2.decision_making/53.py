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

# check votes:
if A_PLUS >= points >= A_MINUS:
    # find differences between two closest constants
   diff_up = abs(A_PLUS - points)
   diff_down = abs(A_MINUS - points)
    # find smaller difference
   diff_min = min(diff_up, diff_down)

    # assign vote
   if diff_min == diff_up:
       vote = "A+"
   else:
       vote = "A-"

elif A_MINUS >= points >= B_PLUS:
   diff_up = abs(A_MINUS - points)
   diff_down = abs(B_PLUS - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "A-"
   else:
       vote = "B+"

elif B_PLUS >= points >= B:
   diff_up = abs(B_PLUS - points)
   diff_down = abs(B - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "B+"
   else:
       vote = "B"

elif B >= points >= B_MINUS:
   diff_up = abs(B - points)
   diff_down = abs(B_MINUS - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "B"
   else:
       vote = "B-"

elif B_MINUS >= points >= C_PLUS:
   diff_up = abs(B_MINUS - points)
   diff_down = abs(C_PLUS - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "B-"
   else:
       vote = "C+"

elif C_PLUS >= points >= C:
   diff_up = abs(C_PLUS - points)
   diff_down = abs(C - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "C+"
   else:
       vote = "C"

elif C >= points >= C_MINUS:
   diff_up = abs(C - points)
   diff_down = abs(C_MINUS - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "C"
   else:
       vote = "C-"

elif C_MINUS >= points >= D_PLUS:
   diff_up = abs(C_MINUS - points)
   diff_down = abs(D_PLUS - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "C-"
   else:
       vote = "D+"

elif D_PLUS >= points >= D:
   diff_up = abs(D_PLUS - points)
   diff_down = abs(D - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "D+"
   else:
       vote = "D"

elif D >= points >= F:
   diff_up = abs(D - points)
   diff_down = abs(F - points)
   diff_min = min(diff_up, diff_down)

   if diff_min == diff_up:
       vote = "D"
   else:
       vote = "F"

# print result
print("Il punteggio", points, "corrisponde al voto", vote)


   




