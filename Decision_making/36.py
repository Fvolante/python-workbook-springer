##
# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog
# years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number.
#

# set conversion's constants
ONE_YEAR = 10.5
TWO_YEAR = ONE_YEAR * 2
OTHER_YEARS = 4

# user's input
dog_years = int(input("Inserisci un numero intero positivo: "))
converted_to_human_years = 0

if dog_years <= 0: # check input is a non negative or 0 integer
    print("Numero inserito errato")
else: # execute on right input
    if dog_years == 1:
        converted_to_human_years = ONE_YEAR
    elif dog_years == 2:
        converted_to_human_years = TWO_YEAR
    else:
        converted_to_human_years = TWO_YEAR + \
                                    (dog_years - 2) * OTHER_YEARS

print("%.1f anni di un cane corrispondono a %.1f anni di un uomo" %(dog_years, converted_to_human_years))                                        
        

