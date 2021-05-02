##
# The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
# spectrum is continuous, it is often divided into 6 colors as shown below:
#
#   Color           Wavelength (nm)
#   ------------------------------------
#   Violet          380 to less than 450
#   Blue            450 to less than 495
#   Green           495 to less than 570
#   Yellow          570 to less than 590
#   Orange          590 to less than 620
#   Red             620 to 750
#
# Write a program that reads a wavelength from the user and reports its color. Display
# an appropriate error message if the wavelength entered by the user is outside of the
# visible spectrum.
#

# user's input
wavelength = int(input("Inserisci la lunghezza d'onda: "))

# set color variable
color = ""

# define color in base of wavelenght
if 380 <= wavelength < 450:
    color = "Viola"
elif 450 <= wavelength < 495:
    color = "Blu"
elif 495 <= wavelength < 570:
    color = "Verde"
elif 570 <= wavelength < 590:
    color = "Giallo"
elif 590 <= wavelength < 620:
    color = "Arancione"
elif 620 <= wavelength <= 750:
    color = "Rosso"
else:
    color = color

# print result
if color == "":
    print("Questa lunghezza d'onda non rientra in uno spettro visibile")
else:
    print("Questa lunghezza d'onda corrisponde al colore", color)
