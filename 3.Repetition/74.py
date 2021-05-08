##
# Write a program that implements Newton’s method to compute and display the
# square root of a number, x, entered by the user. The algorithm for Newton’s method
# follows:
#
# Read x from the user
# Initialize guess to x/2
# While guess is not good enough do
# Update guess to be the average of guess and x/guess
#
# When this algorithm completes, guess contains an approximation of the square
# root of x. The quality of the approximation depends on how you define “good
# enough”. In the author’s solution, guess was considered good enough when the
# absolute value of the difference between guess ∗ guess and x was less than or equal
# to 10**−12.
#

# input and initial variables
x = float(input("Inserisci un numero non negativo: "))
guess = x / 2

# looping until difference is suitable
while abs(guess**2 - x) >= 10e-12:
    guess = (guess + ( x / guess )) / 2

# print result   
print(guess)
