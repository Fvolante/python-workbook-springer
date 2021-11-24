##
# The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
# shown in the table below. The pattern repeats from there, with 2012 being another
# year of the dragon, and 1999 being another year of the hare.
#
#   Year    Animal
#   ----------------
#   2000    Dragon  8
#   2001    Snake   9
#   2002    Horse   10
#   2003    Sheep   11
#   2004    Monkey  0
#   2005    Rooster 1
#   2006    Dog     2
#   2007    Pig     3
#   2008    Rat     4
#   2009    Ox      5
#   2010    Tiger   6
#   2011    Hare    7
#
# Write a program that reads a year from the user and displays the animal associated
# with that year. Your program should work correctly for any year greater than or equal
# to zero, not just the ones listed in the table.
#

# input
year = int(input("Inserisci il tuo anno di nascita: "))

# convert year to 12 remainder
year = year % 12

# assign sign based on remainder 
if year == 8:
    sign = "Drago"
elif year == 9:
    sign = "Serpente"
elif year == 10:
    sign = "Cavallo"
elif year == 11:
    sign = "Pecora"
elif year == 0:
    sign = "Scimmia"
elif year == 1:
    sign = "Gallo"
elif year == 2:
    sign = "Cane"
elif year == 3:
    sign = "Maiale"
elif year == 4:
    sign = "Topo"
elif year == 5:
    sign = "Bue"
elif year == 6:
    sign = "Tigre"
elif year == 7:
    sign = "Lepre"

# print result
print("Il tuo segno zodiacale è", sign)