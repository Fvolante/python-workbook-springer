##
# Create a function that takes an ordinal date, consisting of a year and a day within in
# that year, as its parameters. The function will return the day and month corresponding
# to that ordinal date as its results. Ensure that your function handles leap years
# correctly.
# Use your function, as well as the ordinalDate function that you wrote previously,
# to create a program that reads a date from the user. Then your program should
# report a second date that occurs some number of days later. For example, your program
# could read the date a product was purchased and then report the last date that
# it can be returned (based on a return period that is a particular number of days), or
# your program could compute the due date for a baby based on a gestation period of
# 280 days. Ensure that your program correctly handles cases where the entered date
# and the computed date occur in different years.
#
from es91 import isLeap, ordinalDate, monthDays


def to_gregorianDate(day, year):

    tot_days = 0
    # compunte an average of months the days are covering
    months = day // 30 if day // 30 != 0 else 1

    # set exeption for December
    if months == 12:
        months = 11
    
    # loop on months to compute exact number of days for each month
    for i in range(1, months + 1):
        tot_days = tot_days + monthDays(i, year)

    # manage date comparing to months days 
    day_date = day - tot_days if day >= tot_days else day

    # #
    # manage certain situation of compute dates
    # 
    # case of equal month days and days insert 
    if day_date == 0:
        day_date = monthDays(months, year)
        
    # set months for most common cases
    else:
        months = months + 1

    
    print("Il giorno è:", day_date)
    print("Il mese è:", months)

    

def main():
    print("Inserisci la data:")
    day = int(input("giorno: "))
    month = int(input("mese: "))
    year = int(input("anno: "))

    # convert to ordinal
    days_in_ordinal = ordinalDate(day, month, year)

    # add 60 days of product return back guarantee
    guarantee_date = days_in_ordinal + 60

    # #
    # manage cases when guarantee date goes into new year
    #
    # for leap years
    if isLeap(year) and guarantee_date > 366:
        year = year + guarantee_date // 366
        guarantee_date = guarantee_date % 366

    # for non leap years
    elif guarantee_date > 365:
        year = year + guarantee_date // 365
        guarantee_date = guarantee_date % 365

    # for guarantee dates remaining in curren year
    else:
        pass

    print("Data di ritorno del prodotto (60 giorni):")
    to_gregorianDate(guarantee_date, year)

   
main()