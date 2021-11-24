##
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
# scalene. All three sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of the three sides of a triangle from the
# user. Then display a message that states the triangle’s type.
#

# user's input
side_1 = float(input("Inserisci la misura del primo lato: "))
side_2 = float(input("Inserisci la misura del secondo lato: "))
side_3 = float(input("Inserisci la misura del terzo lato: "))

# set triangle's type
t_type = ""

# check if equilateral
if side_1 == side_2 == side_3:
    t_type = "equilatero"
else:
# check if isosceles
    if side_1 == side_2 or \
        side_1 == side_3 or \
        side_2 == side_3:
        t_type = "isocele"
# check scalene    
    else:
        t_type = "scaleno"

print("Il triangolo è", t_type)