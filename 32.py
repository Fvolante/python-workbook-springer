##
# Develop a program that reads a four-digit integer from the user and displays the sum
# of its digits. For example, if the user enters 3141 then your program should display
# 3+1+4+1=9.
#

# unser's number as string
number = input("Inserisci un numero intero di quattro cifre: ")

# extract each ciphre as int
fir = int(number[0])
sec = int(number[1])
thi = int(number[2])
fou = int(number[3])

# compile sum
sum = fir + sec + thi + fou

# print result
print("La somma delle cifre che compongono il numero" , number, "è:", sum)