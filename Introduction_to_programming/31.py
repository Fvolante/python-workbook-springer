##
# In this exercise you will create a program that reads a pressure from the user in kilopascals.
# Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units.
#
# kPa (kilopascal)
# PSI (Pounds per square inch) 
# mmHg (millimeters of mercury)
# atm (atmospheres)

# kilopascal input
kPa = float(input("Inserisci la pressione in Kilopascal: "))

# conversion
PSI = 0.1450
mmHg = 7.50
atm = 9.869 * (10**-3)

print("%.2f Kilopascal equivalgono a:" %kPa)
print(round(PSI * kPa, 2), "Psi - Pounds per square inch")
print(round(mmHg * kPa, 2), "mmHg - millimeters of mercury")
print(round(atm * kPa, 2), "atm - atmospheres")