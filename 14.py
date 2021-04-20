##
# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
#  
# Hint: One foot is 12 inches. One inch is 2.54 centimeters
#             

# User's feet and inches sizes
user_feet = float(input("Inserisci la parte in piedi della tua altezza: "))
user_inches = float(input("Inserisci la parte in pollici della tua altezza: "))

# Inches and feet conversion to centimetres
INCH_IN_CM = 2.54
FOOT_IN_CM = 12 * INCH_IN_CM
# compute user's sizes to centimetres
user_feet_in_cm = user_feet * FOOT_IN_CM
user_inches_in_cm = user_inches * INCH_IN_CM

# total size in centimetres
total_cm_height = user_feet_in_cm + user_inches_in_cm

print("la tua altezza in centimetri è %i cm" %total_cm_height)