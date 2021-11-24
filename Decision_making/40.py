##
# The following table lists the sound level in decibels for several common noises.
#
# Noise             Decibel Level
# -------------------------------
# Jackhammer        130 dB
# Gas Lawnmower     106 dB
# Alarm Clock       70 dB
# Quiet Room        40 dB

# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the value is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table.
#

# user's input
sound = int(input("Inserisci il livello di rumore in Decibel: "))

# define sound comparison variable
comparison = ""
if sound == 130:
    comparison = "martello pneumatico"
elif sound == 106:
    comparison = "tosaerba"
elif sound == 70:
    comparison = "sveglia"
elif sound == 40:
    comparison = "stanza tranquilla"

# check if sound is too loud or quiet
if sound > 130:
    print("Il tuo rumore è più fragoroso di un martello pneumatico")
elif sound < 40:
    print("Il tuo rumore è più silenzioso di una stanza tranquilla")
# check sound comparisons
else:
    if sound == 130:
        print("Il tuo rumore è quello di un", comparison)   
    elif 130 > sound > 106:
        print("Il tuo rumore è tra un martello pneumatico e un tosaerba")
    elif sound == 106:
        print("Il tuo rumore è quello di un", comparison)
    elif 106 > sound > 70:
        print("Il tuo rumore è tra un tosaerba e una sveglia")
    elif sound == 70:
        print("Il tuo rumore è quello di un", comparison)
    elif 70 > sound > 40:
        print("Il tuo rumore è tra una sveglia e una stanza tranquilla")
    elif sound == 40:
        print("Il tuo rumore è quello di un", comparison)