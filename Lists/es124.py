## 
# A line of best fit is a straight line that best approximates a collection of n data points.
# In this exercise, we will assume that each point in the collection has an x coordinate
# and a y coordinate. The symbols ¯ x and ¯y are used to represent the average x value in
# the collection and the average y value in the collection respectively. The line of best
# fit is represented by the equation y = mx + b where m and b are calculated using
# the following formulas:
# Write a program that reads a collection of points from the user. The user will enter
# the first x coordinate on its own line, followed by the first y coordinate on its own
# line. Allow the user to continue entering coordinates, with the x and y values each
# entered on their own line, until your program reads a blank line for the x coordinate.
# Display the formula for the line of best fit in the form y = mx + b by replacing m
# and b with the values calculated by the preceding formulas. For example, if the user
# inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your program should display
# y = 0.95x + 0.1.

def calculate_m( x, y, n ):
    """
    compute m variable for line of best fit equation
    @params: x,y: lists of coordinates, n: int number of points to evaluate
    @return: number value for m
    """
    
    # set list for xy multiplication
    multiplication_xy = list( map(lambda num_x, num_y: num_x * num_y, x, y ) )

    # set list for x**2 exponentiation
    exponentiation_x2 = list( map(lambda num_x: num_x**2, x) )

    # set numerator and denominator for  final operation
    numerator = sum(multiplication_xy) - ( ( sum(x)  * sum(y) ) / n )
    denominator = sum(exponentiation_x2) - ( ( sum(x)**2 ) / n )

    # return avoiding division by 0 error
    if denominator == 0:
        return 0
    else:
        return numerator / denominator

def calculate_b( x, y, n ):
    """ 
    compute b variable for line of best fit equation
    @params: x,y: lists of coordinates
    @return: number value for b
    """

    # calculate average value for x and y lists and m value
    av_x = sum(x) / len(x)
    av_y = sum(y) / len(y)
    m = calculate_m( x, y, n )
   
    return av_y - m * av_x

def main():

    # set initial variables n:number of points; x,y:lists for points' x and y coordinates
    n = 1
    x = []
    y = []

    # user's inputs until blank line
    coor_x = input("Inserisci la coordinata x per il punto n.%s. Lascia vuoto per terminare: " %n)

    while coor_x != "":

        coor_y = input("Inserisci la coordinata y per il punto n.%s: " %n)

        # compose lists of coordinates
        x.append(float(coor_x))
        y.append(float(coor_y))

        # update variables to continue loop
        coor_x = input("Inserisci la coordinata x per il punto n.%s. Lascia vuoto per terminare: " %(n + 1))
        
        if coor_x != "":
            n += 1 

    # print result
    if not x:
        print("Nessun valore inserito")
    else:
        print( "y = %sx + %s" %( round(calculate_m(x,y,n), 2), round(calculate_b(x,y,n), 2) ) )

main()
