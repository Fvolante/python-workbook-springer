##
# The greatest common divisor of two positive integers, n and m, is the largest number,
# d, which divides evenly into both n and m. There are several algorithms that can be
# used to solve this problem, including:
#
# Initialize d to the smaller of m and n.
# While d does not evenly divide m or d does not evenly divide n do
# Decrease the value of d by 1
# Report d as the greatest common divisor of n and m
#
# Write a program that reads two positive integers from the user and uses this algorithm
# to determine and report their greatest common divisor.
#

# user's inputs
n = int(input("Inserisci un intero positivo per n: "))
m = int(input("Inserisci un intero positivo per m: "))

# set d to smaller
d = min(n, m)

# looping 
while n % d != 0 or m % d != 0:
    d = d - 1

# print result
print(d) 
