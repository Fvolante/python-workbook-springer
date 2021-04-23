##
# In this exercise you will reverse the process described in Exercise 24. Develop a
# program that begins by reading a number of seconds from the user. Then your program
# should display the equivalent amount of time in the form D:HH:MM:SS, where D,
# HH,MM,and SS represent days, hours, minutes and seconds respectively. The hours,
# minutes and seconds should all be formatted so that they occupy exactly two digits.
# Use your research skills determine what additional character needs to be included in
# the format specifier so that leading zeros are used instead of leading spaces when a
# number is formatted to a particular width.
#

# set constants
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

# user's input
user_seconds = int(input("Inserisci il numero di secondi: "))


days = user_seconds // DAY
days_left_in_sec = user_seconds % DAY

hours = days_left_in_sec // HOUR
hours_left_in_sec = days_left_in_sec % HOUR

minutes = hours_left_in_sec // MINUTE
min_left_in_sec = hours_left_in_sec % MINUTE

seconds = min_left_in_sec // SECOND

# result
print("%i secondi equivalgono a:" %user_seconds)
print("%02i giorni" %days)
print("%02i ore" %hours)
print("%02i minuti e" %minutes)
print("%02i secondi" %seconds)

