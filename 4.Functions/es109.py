##
# A magic date is a date where the day multiplied by the month is equal to the two digit
# year. For example, June 10, 1960 is amagic date because June is the sixth month, and
# 6 times 10 is 60, which is equal to the two digit year. Write a function that determines
# whether or not a date is a magic date. Use your function to create a main program
# that finds and displays all of the magic dates in the 20th century. You will probably
# find your solution to Exercise 106 helpful when completing this exercise.


from es91 import monthDays

def isMagicDate(day, month, year):

    year = str(year)
    last_two_digits = int(year[-2:])
    
    if day * month == last_two_digits:
        return True
    else:
        return False

def main():

    for year in range(1900, 2000):
        
        for month in range(1, 13):

            days = monthDays(month, year) + 1

            for day in range(1, days):

                if isMagicDate(day, month, year):
                    print(day, month, year)

main()