##
# A univariate quadratic function has the form f (x) = ax2 +bx +c, where a, b and c
# are constants, and a is non-zero. Its roots can be identified by finding the values of x
# that satisfy the quadratic equation ax2 +bx +c = 0. These values can be computed
# using the quadratic formula, shown below. A quadratic function may have 0, 1 or 2
# real roots.
#
#    
#
# The portion of the expression under the square root sign is called the discriminant.
# If the discriminant is negative then the quadratic equation does not have any real
# roots. If the discriminant is 0, then the equation has one real root. Otherwise the
# equation has two real roots, and the expression must be evaluated twice, once using
# a plus sign, and once using a minus sign, when computing the numerator.
# Write a program that computes the real roots of a quadratic function. Your program
# should begin by prompting the user for the values of a, b and c. Then it should
# display a message indicating the number of real roots, along with the values of the
# real roots (if any).
#
from cmath import sqrt

# inputs
a = float(input("Inserisci il valore di a (diverso da 0): "))

if a == 0:
    print("Valore errato")
    quit()

b = float(input("Inserisci il valore di b: "))
c = float(input("Inserisci il valore di c: "))

# compute discriminant
discr = (b ** 2) - (4 * a * c)

# two solution for discr > 0
if discr > 0:
    root_pos = (-b +sqrt(discr)) / (2 * a)
    root_neg = (-b -sqrt(discr)) / (2 * a)
    print("il discriminante è %s e la funzione ha due radici: %s e %s" %(discr, root_pos, root_neg))

# one solution for discr == 0
elif discr == 0:
    root = (-b / 2 * a)
    print("Il discriminante è 0 e la funzione ha una singola radice:", root)

# no solution for discr < 0
else:
    print("La funzione quadratica non ha radici reali")
 

