##
# Positions on a chess board are identified by a letter and a number. The letter identifies
# the column, while the number identifies the row, as shown below:
#
# Write a program that reads a position from the user. Use an if statement to
# determine if the column begins with a black square or a white square. Then use
# modular arithmetic to report the color of the square in that row. For example, if the
# user enters a1 then your program should report that the square is black. If the user
# enters d5 then your program should report that the square is white. Your program
# may assume that a valid position will always be entered. It does not need to perform
# any error checking.
#

# user's row input
row = int(input("Inserisci il numero di riga: "))

# convert col letter to unicode char number
col = input("Inserisci la lettera della colonna: ")
col = ord(col.lower())


# set math const
WHITE = -1
BLACK = 1

# convert row to math const
if row % 2 == 0:
    row = WHITE
else:
    row = BLACK

# convert col to math const
if col % 2 == 0:
    col = WHITE
else:
    col = BLACK

# compute square
square = col * row

if square == -1:
    square = "white"
else:
    square = "black"

# print result
print("La casella selezionata è", square)