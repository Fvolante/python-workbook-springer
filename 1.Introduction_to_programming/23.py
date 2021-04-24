##
# A polygon is regular if its sides are all the same length and the angles between all of
# the adjacent sides are equal. The area of a regular polygon can be computed using
# the following formula, where s is the length of a side and n is the number of sides:
#
#   area = (n × s**2) / 4 * tan( math.pi / n)
#
# Write a program that reads s and n from the user and then displays the area of a
# regular polygon constructed from these values.        
#

from math import pi, tan

# user's input
s = float(input("Inserisci la lunghezza dei lati del poligono: "))
n = int(input("Inserisci il numero di lati del poligono: "))

# compute area
area = (n * s**2) / 4 * tan(pi / n)

print("I'area del poligono di %i lati di lunghezza %.2f è %.2f" %(n, s, area))