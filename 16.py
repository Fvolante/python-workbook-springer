##
# Write a program that begins by reading a radius, r , from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r . Use the pi constant in the math module in your
# calculations.
#
# Hint: The area of a circle is computed using the formula area = πr**2. The
# volume of a sphere is computed using the formula volume = 4/3 * πr ** 3
# 

import math

# user's radius input 
radius = float( input("Inserisci il raggio: ") )

#compute circle's area
area = math.pi * (radius ** 2)

#compute sphere's volume
volume = (4 / 3) * (math.pi * (radius ** 3) )

print("I'area è: %.2f\nil volume è: %.2f" %(area, volume))