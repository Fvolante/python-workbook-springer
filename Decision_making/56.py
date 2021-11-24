##
# Electromagnetic radiation can be classified into one of 7 categories according to its
# frequency, as shown in the table below:
# 
#   Name                Frequency Range (Hz)
#   ----------------------------------------------------------
#   Radio Waves         Less than 3 × 10**9
#   Microwaves          3 × 10**9 to less than 3 × 10**12
#   Infrared Light      3 × 10**12 to less than 4.3 × 10**14
#   Visible Light       4.3 × 10**14 to less than 7.5 × 10**14
#   Ultraviolet Light   7.5 × 10**14 to less than 3 × 10**17
#   X-Rays              3 × 10**17 to less than 3 × 10**19
#   Gamma Rays          3 × 10**19 or more
#
# Write a program that reads the frequency of some radiation from the user and
# displays name of the radiation as part of an appropriate message.
#

# user's input
user_frq = float(input("Inserisci la frequenza in GHz: "))

# convert Ghz to HZ
HZ = 1e9
frq = user_frq * HZ

# check type of radiations
if frq < 3e9:
    name = "onde radio"
elif 3e9 <= frq < 3e12:
    name = "microonde"
elif 3e12 <= frq < 4.3e14:
    name = "microonde"
elif 4.3e12 <= frq < 7.5e14:
    name = "spettro visibile"
elif 7.5e14 <= frq < 3e17:
    name = "raggi ultravioletti"
elif 3e17 <= frq < 3e19:
    name = "raggi X"
elif 3e19 <= frq :
    name = "raggi Gamma"
else:
    name = ""

# print result
if name == "":
    print("La frequenza delle radiazioni non rientra in questo spettro")
else:
    print("La frequenza di", user_frq, "Ghz corrisponde a:", name)
    




