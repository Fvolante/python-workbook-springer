##
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
#     sum = (n)(n + 1) / 2
#              
#

n = int( input("Inserisci un numero intero positivo: ") )

sum = (n * ( n + 1 )) / 2

print("La somma di tutti i numeri da 1 a", "%i" %n, "è", "%i" %sum)