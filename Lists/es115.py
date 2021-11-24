## 
# A proper divisor of a positive integer, n, is a positive integer less than n which divides
# evenly into n. Write a function that computes all of the proper divisors of a positive
# integer. The integer will be passed to the function as its only parameter. The function
# will return a list containing all of the proper divisors as its only result. Complete
# this exercise by writing a main program that demonstrates the function by reading
# a value from the user and displaying the list of its proper divisors. Ensure that your
# main program only runs when your solution has not been imported into another file.

""" 
return a list of proper divisor of a positive int
@param: a positive int
@return: list of proper divisor
 """
def proper_divisors(integer):

    # set result list
    divisors = [] 

    # loop on each integers from 2 to parameter value and add to result lis if proper divisor
    for i in range(1, integer):
        
        if integer % i == 0:
            divisors.append(i)

    #return list
    return divisors

def main():
    value = int(input("Inserisci un intero positivo:"))

    print("I divisori di", value, "sono:")
    print(proper_divisors(value))

if __name__ == "__main__":
    main()


