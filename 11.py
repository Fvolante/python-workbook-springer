##
# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon
# (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPGto L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.
#
# L/100 km = 235.21 / MPG 
#              


MPG = float(input("Inserisci il tuo valore di MPG: "))

Lp100KM = 235.21 / MPG

print("Il valore convertito di %i" %MPG, "MPG in Litri per 100 km è: %.2f" %Lp100KM)





