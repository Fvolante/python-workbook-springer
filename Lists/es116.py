## 
# An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
# equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
# 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
# Write a function that determines whether or not a positive integer is perfect. Your
# function will take one parameter. If that parameter is a perfect number then your
# function will return True. Otherwise it will return False. In addition, write a main
# program that uses your function to identify and display all of the perfect numbers
# between 1 and 10,000. Import your solution to Exercise 115 when completing this
# task.

from es115 import proper_divisors

""" 
check if a positive integers is perfect
@param: a positive int
@return: bool
 """
def is_perfect_int(integer):

    """ 
    concise form with ternary operator:

    return True if (sum(proper_divisors(integer)) == integer) else False 
    """

    # sum all proper divisors of argument
    integers_sum = sum(proper_divisors(integer))

    # check and return
    if integers_sum == integer:
        return True
    else:
        return False


# all perfect numbers to 10000
def main():

    print("I numeri perfetti tra 1 e 10000 sono:")

    for i in range(1, 10001):

        if is_perfect_int(i):
            print(i)

main()  