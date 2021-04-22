##
# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.
#

# set constants
SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE
DAY = 24 * HOUR

# user's input
days = int(input("Inserisci il numero di giorni: "))
hours = int(input("Inserisci il numero di ore: "))
minutes = int(input("Inserisci il numero di minuti: "))
seconds = int(input("Inserisci il numero di secondi: "))

result_in_seconds = (days * DAY) + (hours * HOUR) + (minutes * MINUTE) + (seconds * SECOND)

# print result
print(result_in_seconds)
