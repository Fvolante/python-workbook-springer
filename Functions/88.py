##
# Write a function that takes three numbers as parameters, and returns the median value
# of those parameters as its result. Include a main program that reads three values from
# the user and displays their median.
#
# Hint: The median value is the middle of the three values when they are sorted
# into ascending order. It can be found using if statements, or with a little bit of
# mathematical creativity.
#


def calc_med(a, b, c):
    # values sum
    summ = a + b + c

    # find max and min value
    mi = min(a, b, c)
    ma = max(a, b, c)

    # find med value
    return summ - mi - ma

def main():
    a = float(input("Inserisci un valore per a: "))
    b = float(input("Inserisci un valore per b: "))
    c = float(input("Inserisci un valore per c: ")) 

    #print result
    print("Il valore mediano è:", calc_med(a, b, c))

if __name__ == "__main__":
    main()
