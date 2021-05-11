##
# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
# for every 140 meters travelled. Write a function that takes the distance travelled (in
# kilometers) as its only parameter and returns the total fare as its only result. Write a
# main program that demonstrates the function.
#
#  Hint: Taxi fares change over time. Use constants to represent the base fare and
#  the variable portion of the fare so that the program can be updated easily when
#  the rates increase.
#

# set constants
BASE_FARE = 4.00
EXTRA_FARE = 0.25
   
def calc_fare(distance):

    # convert km to metres
    distance = distance * 1000
    metres_to_pay = distance / 140
    print(metres_to_pay)

    # compute fare and return
    return round(BASE_FARE + (EXTRA_FARE * metres_to_pay), 2)
    
def main():

    # input
    distance = float(input("Inserisci la distanza percorsa in km: "))

    # print result
    print("Il costo del viaggio è %s euri" %calc_fare(distance))

if __name__ == "__main__":
    main()
