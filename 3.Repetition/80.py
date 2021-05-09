##
# The prime factorization of an integer, n, can be determined using the following steps:
#
# Initialize factor to 2
# While factor is less than or equal to n do
# If n is evenly divisible by factor then
# Conclude that factor is a factor of n
# Divide n by factor using floor division
# Else
# Increase factor by 1
#
# Write a program that reads an integer from the user. If the value entered by the
# user is less than 2 then your program should display an appropriate error message.
# Otherwise your program should display the prime numbers that can be multiplied
# together to compute n, with one factor appearing on each line. For example:
#
# Enter an integer (2 or greater): 72
# The prime factors of 72 are:
# 2
# 2
# 2
# 3
# 3
#

n = int(input("Inserisci un numero da 2 in su: "))
f = 2

# looping until insert integer greater than 2
while True:
    if n < 2:
        print("Il numero inserito non è corretto")
        n = int(input("Inserisci un numero da 2 in su: "))
    else:
        break

# print first line and start computation
print("I fattori primi di", n, "sono: ")
while f <= n:

    if n % f == 0:
        print(f)
        n = n / f
    else:
        f = f + 1

