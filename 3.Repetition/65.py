##
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the Internet.
#

# set and draw headings
heading = "| CELSIUS | FARHENEIT |"

print("-" * len(heading))
print(heading)
print("-" * len(heading))

for cel in range(10, 101, 10):
    
    # compute conversion
    far = 1.8 * cel + 32

    # draw results in rows
    print("|%5s    |%8s   |" %(cel, far))
    print("-" * len(heading))