##
# Write a program that asks the user to enter the width and length of a room. Once
# these values have been read, your program should compute and display the area of
# the room. The length and the width will be entered as floating-point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.
#

width = float( input("Inserire la larghezza in metri: ") )
length = float( input("Inserire la lunghezza in metri: ") )
area = width * length

print("L'area della stanza è", "%.2f" %area + " metri")