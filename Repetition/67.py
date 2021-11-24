##
# Write a program that computes the perimeter of a polygon. Begin by reading the
# x and y coordinates for the first point on the perimeter of the polygon from the
# user. Then continue reading pairs of values until the user enters a blank line for the
# x-coordinate. Each time you read an additional coordinate you should compute the
# distance to the previous point and add it to the perimeter. When a blank line is entered
# for the x-coordinate your program should add the distance from the last point back
# to the first point to the perimeter. Then the perimeter should be displayed. Sample
# input and output values are shown below. The input values entered by the user are
# shown in bold.
#
# Enter the first x-coordinate: 0
# Enter the first y-coordinate: 0
# Enter the next x-coordinate (blank to quit): 1
# Enter the next y-coordinate: 0
# Enter the next x-coordinate (blank to quit): 0
# Enter the next y-coordinate: 1
# Enter the next x-coordinate (blank to quit):
# The perimeter of that polygon is 3.414213562373095  
# 
from math import sqrt

# set coordinates for first point
start_x = input("Inserisci la prima coordinata del punto x: ")
start_y = input("Inserisci la prima coordinata del punto y: ")

# set initial coordinates to start looping
x1 = start_x
y1 = start_y
x2 = 0
y2 = 0
perimeter = 0

# loop until "" is insert
while x1 != "":
    # convert strings to float to compute (need also for y1 initial variable coming outside the loop)
    x1 = float(x1)
    y1 = float(y1)

    # insert new point coordinates
    x2 = input("Inserisci la coordinata del punto x seguente (in bianco per uscire): ")

    # continue if value is not blank
    if x2 != "":
        x2 = float(x2)
        y2 = float(input("Inserisci la coordinata del punto y seguente: "))

        # compute progessive perimeter
        perimeter = perimeter + (sqrt((x2-x1)**2 + (y2-y1)**2))
    else:
        # compute last side of polygon
        perimeter = perimeter + (sqrt((x1-float(start_x))**2 + (y1-float(start_y))**2))

    # assign to first numbers variable to restart the loop
    x1 = x2
    y1 = y2
    
# print result
print("Il perimetro del poligono è:", perimeter)