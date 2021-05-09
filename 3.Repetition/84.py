##
# What’s the minimum number of times you have to flip a coin before you can have
# three consecutive flips that result in the same outcome (either all three are heads or
# all three are tails)? What’s the maximum number of flips that might be needed? How
# many flips are needed on average? In this exercise we will explore these questions
# by creating a program that simulates several series of coin flips.
# Create a program that uses Python’s random number generator to simulate flipping
# a coin several times. The simulated coin should be fair, meaning that the probability
# of heads is equal to the probability of tails. Your program should flip simulated
# coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
# time the outcome is heads, and a T each time the outcome is tails, with all of the
# outcomes for one simulation on the same line. Then display the number of flips that
# were needed to reach 3 consecutive occurrences of the same outcome. When your
# program is run it should perform the simulation 10 times and report the average
# number of flips needed. Sample output is shown below:
#
# H T T T (4 flips)
# H H T T H T H T T H H T H T T H T T T (19 flips)
# T T T (3 flips)
# T H H H (4 flips)
# H H H (3 flips)
# T H T T H T H H T T H H T H T H H H (18 flips)
# H T T H H H (6 flips)
# T H T T T (5 flips)
# T T H T T H T H T H H H (12 flips)
# T H T T T (5 flips)
# On average, 7.9 flips were needed.
#

from random import randint

# set const strings and total flips counter
HEAD = "H "
TAIL = "T "
total_flips = 0

# loop 10 series
for i in range(0, 10):

    # set initial counter varibles
    heads_count = 0
    tails_count = 0
    old_flip = ""
    flip_count = 0
    
    # loop current serie
    while heads_count < 3 and tails_count < 3:

        # assign head or tail to current flip
        current_flip = HEAD if randint(1, 2) == 1 else TAIL

        # increase heads or tails counter if current flip is same as old
        if current_flip == old_flip and current_flip == HEAD:
            heads_count += 1
            print(current_flip, end="")

        elif current_flip == old_flip and current_flip == TAIL:
            tails_count += 1
            print(current_flip, end="")

        # behaviour if new flip is different from previous
        else:

            if current_flip == HEAD:
                heads_count += 1
                tails_count = 0
            else:
                tails_count += 1
                heads_count = 0

            print(current_flip, end="")

        # set current flip as old for next iteration purposes
        old_flip = current_flip
        # increase amount of this serie's flips
        flip_count += 1

    # at the end of serie, display current serie's flips' amount
    print("(", flip_count, "flips )")
    # increase amount of flips of every series for average purpose
    total_flips = total_flips + flip_count

# compute average of flips and display
average = total_flips / 10
print("Tot flips:", total_flips)
print("Media:", average)