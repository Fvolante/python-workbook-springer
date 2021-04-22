##
# The area of a triangle can be computed using the following formula, where b is the
# length of the base of the triangle, and h is its height:
# area = (b × h) / 2
# Write a program that allows the user to enter values for b and h. The program should
# then compute and display the area of a triangle with base length b and height h. 
#

# user's input
b = float(input("Inserisci la misura della base del triangolo: "))
h = float(input("Inserisci la misura dell'altezza del triangolo: "))

# compute area
area = (b * h) / 2

print("L'area del triangolo di base %.2f e altezza %.2f è %.2f" %(b, h, area))