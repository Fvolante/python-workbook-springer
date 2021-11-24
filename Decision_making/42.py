##
# The following table lists an octave of music notes, beginning with middle C, along
# with their frequencies.
#
#   Note    Frequency (Hz)
#   ----------------------
#   C4      261.63
#   D4      293.66
#   E4      329.63
#   F4      349.23
#   G4      392.00
#   A4      440.00
#   B4      493.88
#
# Begin by writing a program that reads the name of a note from the user and
# displays the note’s frequency. Your program should support all of the notes listed
# previously.
# Once you have your program working correctly for the notes listed previously
# you should add support for all of the notes from C0 to C8. While this could be
# done by adding many additional cases to your if statement, such a solution is
# cumbersome, inelegant and unacceptable for the purposes of this exercise. Instead,
# you should exploit the relationship between notes in adjacent octaves. In particular,
# the frequency of any note in octave n is half the frequency of the corresponding
# note in octave n + 1. By using this relationship, you should be able to
# add support for the additional notes without adding additional cases to your if
# statement.   
#
#   Hint: You will want to access the characters in the note entered by the user
#    individually when completing this exercise. Begin by separating the letter from
#    the octave. Then compute the frequency for that letter in the fourth octave using
#    the data in the table above. Once you have this frequency you should divide it
#    by 2**(4−x) , where x is the octave number entered by the user. This will halve or
#    double the frequency the correct number of times.
#

# user's input
note = input("Inserisci la nota: ")
note = note.upper()

# create 4 octave constants
C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

# create frequency variable
frq = 0

# create variable separating letter and octave
note_letter = note[0]
note_octave = int(note[-1])

# compute frequencies starting from 4 octave
if note_letter == "A":
    frq = A4
elif note_letter == "B":
    frq = B4
elif note_letter == "C":
    frq = C4
elif note_letter == "D":
    frq = D4
elif note_letter == "E":
    frq = E4
elif note_letter == "F":
    frq = F4
elif note_letter == "G":
    frq = G4

# compute frequency 
frq = frq /  2 ** (4-note_octave)
frq = round(frq, 2)

# print result
print("La frequenza della nota", note, "è", frq)