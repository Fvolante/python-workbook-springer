##
# Create a program that reads two integers, a and b, from the user.Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of a**b
#
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list
#              

import math

a = int(input("Inserisci l'intero a: "))
b = int(input("Inserisci l'intero b: "))

sum = a + b
diff = a - b
prod = a * b
quotient = a / b
remaind = a % b
log10 = math.log10(a)
pot = a ** b

print("La somma di a + b è:", sum)
print("La differenza di a - b è:", diff)
print("Il prodotto di a e b è:", prod)
print("Il quoziente di a diviso b è:", "%.2f" %quotient)
print("Il resto di a diviso b è:", "%.2f" %remaind)
print("Il logaritmo base 10 di a è:", "%.2f" %log10)
print("La potenza di a per b è:", pot)




