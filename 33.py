##
# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.
#

fir = int(input("Inserisci il primo numero: "))
sec = int(input("Inserisci il secondo numero: "))
thi = int(input("Inserisci il terzo numero: "))

# find min and max value
min_n = min(fir, sec, thi)
max_n = max(fir, sec, thi)

# find middle value
sum_v = fir + sec + thi
middle = sum_v - max_n - min_n

# print result
print("Il numero più alto è:", max_n)
print("Il numero più basso è:", min_n)
print("Il numero di mezzo è:", middle)
