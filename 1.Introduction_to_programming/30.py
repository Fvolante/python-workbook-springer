##
# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the Internet.
#
#   0 °C + 273.15 kelvin
#   (0 °C × 9/5) + 32 farheneit
#

# user's input
celsius = float(input("Inserisci la temperatura in C°: "))

# convesrion
kel = celsius + 273.15
far = ( celsius * 9/5 ) + 32

# result
print("%.2f gradi Celsius corrispondono a \n%.2f Kelvin e \n%.2f Farheneit" %(celsius, kel, far))