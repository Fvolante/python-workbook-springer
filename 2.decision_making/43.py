##
# In the previous question you converted from a note’s name to its frequency. In this
# question you will write a program that reverses that process. Begin by reading a
# frequency from the user. If the frequency is within one Hertz of a value listed in
# the table in the previous question then report the name of the corresponding note.
# Otherwise report that the frequency does not correspond to a known note. In this
# exercise you only need to consider the notes listed in the table. There is no need to
# consider notes from other octaves.
#

frq = float(input("Inserisci la frequenza in Hz: "))

# create 4 octave constants
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

# create name variable
note = ""

# check notes' frequency
if C4 - 1 <= frq <= C4 + 1 :
    note = "C4"
elif D4 - 1 <= frq <= D4 + 1 :
    note = "D4"
elif E4 - 1 <= frq <= E4 + 1 :
    note = "E4"
elif F4 - 1 <= frq <= F4 + 1 :
    note = "F4"
elif G4 - 1 <= frq <= G4 + 1 :
    note = "G4"
elif A4 - 1 <= frq <= A4 + 1 :
    note = "A4"
elif B4 - 1 <= frq <= B4 + 1 :
    note = "B4"
else:
    print("Frequenza non supportata in questo software")

# print note's name
if note != "":
    print("La frequenza", frq, "corrisponde alla nota", note)


