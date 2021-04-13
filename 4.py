##
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# 
# Hint: There are 43,560 square feet in an acre.
#

length = float( input("Inserisci la lunghezza in piedi: ") )
width = float( input("Inserisci la larghezza in piedi: ") )

area = length * width
acres = area / 43560


print("Il campo misura", "%.2f" %acres, "acri")