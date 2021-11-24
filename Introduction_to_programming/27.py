##
# Easter is celebrated on the Sunday immediately after the first full moon following the
# spring equinox. Because its date includes a lunar component, Easter does not have
# a fixed date in the Gregorian calendar. Instead, it can occur on any date between
# March 22 and April 25. The month and day for Easter can be computed for a given
# year using the Anonymous Gregorian Computus algorithm, which is shown below.
# Write a program that implements the Anonymous Gregorian Computus algorithm
# to compute the date of Easter. Your program should read the year from the user and
# then display a appropriate message that includes the date of Easter in that year.

# user's year input:
year = int(input("Inserisci l'anno per cui vuoi ottenere la data di Pasqua: "))

# Anonymous Gregorian Computus algorithm
a = year % 19
b = year // 100
c = year % 100
d = b // 4
e = b % 4
f = (b + 8) // 25
g = (b - f + 1) // 3
h = ( (19 * a) + b - d - g + 15) % 30
i = c // 4
k = c % 4
l = ( 32 + (2 * e) + (2 * i) - h - k ) % 7
m = ( a + (11 * h) + (22 * l) ) // 451
month = ( h + l - (7 * m) + 114 ) // 31
day = 1 + ( ( h + l - (7 * m) + 114 ) % 31 )

print("Nell' anno %i la Pasqua cade nel giorno %02i %02i" %(year, day, month))