##
# The value of π can be approximated by the following infinite series:
# 
# Write a program that displays 15 approximations of π. The first approximation
# should make use of only the first term from the infinite series. Each additional
# approximation displayed by your program should include one more term in the series,
# making it a better approximation of π than any of the approximations displayed previously.

# set initial counter variables
seq = 0
term_number = 0

# loop with 2 step until 15 repetions are done
for i in range(2, 32, 2):
    
    term_number = term_number + 1
    
    # set terms for every repetition
    term = 4 / ( (i) * (i + 1) * (i + 2) ) 
    term = term if term_number % 2 != 0 else -abs(term)

    # compute progressive sequence of terms
    seq = seq + term 
    
    # print progessive approssimation of pi
    print("pi:", 3 + seq)
    print("")
    