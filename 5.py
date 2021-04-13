##
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and two digits to the right of the decimal point.
#

liter_or_less = float( input("Vuoti di un litro o meno hai: ") )
more_than_liter = float( input("Vuoti di più di un litro: ") )

less_refund = 0.10 * liter_or_less
more_refund = 0.25 * more_than_liter
total_refund = less_refund + more_refund

print("Hai diritto a un rimborso di $", "%.2f" %total_refund, "dolla")

