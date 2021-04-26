##
# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.
#

# user's input
sides = int(input("Inserisci il numero di lati della figura: "))

# fugure's name
shape = ""

if sides == 3:
    shape = "Triangolo"
elif sides == 4:
    shape = "Quadrato"
elif sides == 5:
    shape = "Pentagono"
elif sides == 6:
    shape = "Esagono"
elif sides == 7:
    shape = "Ettagono"
elif sides == 8:
    shape = "Ottagono"
elif sides == 9:
    shape = "Enneagono"
elif sides == 10:
    shape = "Decagono"
else:
    print("Numero di lati sbagliato")

# print if the figure has a name
if shape != "":
    print("La figura con %i lati è un" %sides, shape) 