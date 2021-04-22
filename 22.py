##
# In the previous exercise you created a program that computed the area of a triangle
# when the length of its base and its height were known. It is also possible to compute
# the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
# be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
# can be calculated using the following formula:
#
#   area = math.sqrt(s × (s − s1) × (s − s2) × (s − s3))
#
# Develop a program that reads the lengths of the sides of a triangle from the user and
# displays its area.
#

from math import sqrt

# user's input
s1 = float(input("Inserisci il primo lato del triangolo: "))
s2 = float(input("Inserisci il secondo lato del triangolo: "))
s3 = float(input("Inserisci il terzo lato del triangolo: "))

# compute s
s = (s1 + s2 + s3) / 2

# compute area
area = sqrt(s * (s - s1) * (s - s2) * (s - s3))

print("L'area del triangolo con lati %.2f, %.2f, %.2f è %.2f" %(s1, s2, s3, area))