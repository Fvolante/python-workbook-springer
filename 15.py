##
# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.
#
# 1 yard = 3 feet
# 1 mile = 1760 yards

FEET = 1
YARD = FEET * 3
MILE = 1760 * YARD

feet_input = float(input("Inserisci la misura in piedi: "))

feets = feet_input % YARD
yards = feet_input // YARD
yards_rest = yards % 1760
miles = feet_input // MILE

print("Il valore è %i miglia, %i yarde e %i piedi" %(miles, yards_rest, feets) )