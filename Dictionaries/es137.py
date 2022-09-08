# In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function
# that simulates rolling a pair of six-sided dice. Your function will not take any
# parameters. It will return the total that was rolled on two dice as its only result.
# Write a main program that uses your function to simulate rolling two six-sided
# dice 1,000 times. As your program runs, it should count the number of times that
# each total occurs. Then it should display a table that summarizes this data. Express
# the frequency for each total as a percentage of the number of rolls performed. Your
# program should also display the percentage expected by probability theory for each
# total. Sample output is shown below.
#
#           Total       Simulated       Expected
#                       Percent         Percent
#           2           2.90            2.78
#           3           6.90            5.56
#           4           9.40            8.33
#           5           11.90           11.11
#           6           14.20           13.89
#           7           14.20           16.67
#           8           15.00           13.89
#           9           10.50           11.11
#           10          7.90            8.33
#           11          4.50            5.56
#           12          2.60            2.78
import random

""" 
simulate a roll of a pair fi dice
@return int: the sum of the two results of dices' rolling
"""
def roll_two_dices():

    # roll two dices and return sum
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    return dice1 + dice2

def main():

    # set final dict result
    dices_counts = {}

    for dice_launch in range(1000):

        dices_result = roll_two_dices()

        # add counts to dictonary
        # 1) if/else statement version
        """ if dices_result in dices_counts:
            dices_counts[dices_result] += 1

        else:
            dices_counts[dices_result] = 0 """

        # 2) using get method: return 0 or increase the counter
        dices_counts[dices_result] = dices_counts.get(dices_result, 0) + 1

    # convert number of shots to percentage, rounding to 2 points float number
    for key in dices_counts:
        
        dices_counts[key] = str(round((dices_counts[key] / 1000) * 100, 2)) + "0"  

    expected_percent = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]

    for key in sorted(dices_counts):
        print(f"{key:<10} {dices_counts[key]:<10}", end=" " * 8)
        print(expected_percent[key-2])    

main()





















#print('''
#Total       Simulated       Expected
#            Percent         Percent
#''')

d = {
    1: ["Python", 33.2, 'UP'], 
    2: ["Java", 23.54, 'DOWN'], 
    3: ["Ruby", 17.22, 'UP'], 
    10: ["Lua", 10.55, 'DOWN'],
    5: ["Groovy", 9.22, 'DOWN'],
    6: ["C", 1.55, 'UP']
}
#print("{} {} {}".format("Total\n", "Simulated\nPercent\n", "Expected\nPercent"))
""" print("Total\n", end=" "*10)
print("Simulated\n"+ " "*15 + "Percent\n", end="")
print("Expected\nPercent", end=" ") """
#print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Lang','Percent','Change'))