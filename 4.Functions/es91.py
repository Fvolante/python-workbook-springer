##
# An ordinal date consists of a year and a day within it, both of which are integers. The
# year can be any year in the Gregorian calendar while the day within the year ranges
# from one, which represents January 1, through to 365 (or 366 if the year is a leap
# year) which represents December 31. Ordinal dates are convenient when computing
# differences between dates that are a specific number of days (rather than months). For
# example, ordinal dates can be used to easily determine whether a customer is within
# a 90 day return period, the sell-by date for a food-product based on its production
# date, and the due date for a baby.
# Write a function named ordinalDate that takes three integers as parameters.
# These parameters will be a day, month and year respectively. The function should
# return the day within the year for that date as its only result. Create a main program
# that reads a day,month and year from the user and displays the day within the year for
# that date. Your main program should only run when your file has not been imported
# into another program.
#


##
# define if a year is leap or not
# @param year to check
# @bool if year is leap
#

def isLeap(year):
    
    is_leap = False

    # leap check
    if year % 400 == 0:
        is_leap = True
    elif year % 100 == 0:
        is_leap = False
    elif year % 4 == 0:
        is_leap = True
    else:
        is_leap = False

    return is_leap

##
# finnd exact number of days of single month
# @param int month to check
# @param year int to check leap or not
# @int number of days
#    

def monthDays(month, year):

    if month == 4 or month == 6 or \
        month == 9 or month == 11:

        month_days = 30

    elif month == 2:
        if isLeap(year):
            month_days = 29
        else:
            month_days = 28

    else:
        month_days = 31

    return month_days

##
# convert a gregorian date to ordinal one
# @param int day to convert
# @param int month to check
# @param year int to check leap or not
# @return int number of days
#    
def ordinalDate(day, month, year):

    # set initial varibile for compute days
    final_days = 0

    # progressively add days to total days
    for i in range(1, month):
        final_days = final_days + monthDays(i, year)

    # result
    return final_days + day
    
def main():
    
    day = int(input("Inserisci il giorno: "))
    month = int(input("Inserisci il mese: "))
    year = int(input("Inserisci l'anno: "))

    print("La data corrisponde a: %i-%i" %(ordinalDate(day, month, year), year))

if __name__ == "__main__":
    main()