##
# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.
#             
import math

radius = float(input("Inserisci l'area del cerchio alla base del cilindro: "))
height = float(input("Inserisci l'altezza del cilindro: "))

# compute circle's area
circle_area = math.pi * (radius ** 2)

# compute volume of cylinder
volume = circle_area * height

print("Il volume del cilindro di raggio %.2f e altezza %.2f è %.1f" % (radius, height, volume))