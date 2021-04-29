##
# The horoscopes commonly reported in newspapers use the position of the sun at the
# time of one’s birth to try and predict the future. This system of astrology divides the
# year into twelve zodiac signs, as outline in the table below:
#
#       Zodiac Sign     Date Range
#       ------------------------------------------
#       Capricorn       December 22 to January 19
#       Aquarius        January 20 to February 18
#       Pisces          February 19 to March 20
#       Aries           March 21 to April 19
#       Taurus          April 20 to May 20
#       Gemini          May 21 to June 20
#       Cancer          June 21 to July 22
#       Leo             July 23 to August 22
#       Virgo           August 23 to September 22
#       Libra           September 23 to October 22
#       Scorpio         October 23 to November 21
#       Sagittarius     November 22 to December 21
#
# Write a program that asks the user to enter his or her month and day of birth. Then
# your program should report the user’s zodiac sign as part of an appropriate output
# message.
#

# inputs
day = int(input("Inserisci il tuo giorno di nascita: "))
month = input("Inserisci il tuo mese di nascita: ")

# check signs
if month == "dicembre":
    sign = "Capricorno" if day >= 22 else "Sagittario"
elif month == "gennaio":
    sign = "Acquario" if day >= 20 else "Capricorno"
elif month == "febbraio":
    sign = "Pesci" if day >= 19 else "Acquario"
elif month == "marzo":
    sign = "Ariete" if day >= 21 else "Pesci"
elif month == "aprile":
    sign = "Toro" if day >= 20 else "Ariete"
elif month == "maggio":
    sign = "Gemelli" if day >= 21 else "Toro"
elif month == "giugno":
    sign = "Cancro" if day >= 21 else "Gemelli"
elif month == "luglio":
    sign = "Leone" if day >= 23 else "Cancro"
elif month == "agosto":
    sign = "Vergine" if day >= 23 else "Leone"
elif month == "settembre":
    sign = "Bilancia" if day >= 23 else "Vergine"
elif month == "ottobre":
    sign = "Scorpione" if day >= 23 else "Bilancia"
elif month == "novembre":
    sign = "Sagittario" if day >= 22 else "Scorpione"

# print result
print("Il tuo segno zodiacale è", sign)