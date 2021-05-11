##
# The Twelve Days of Christmas is a repetitive song that describes an increasingly
# long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
# the first day. A new gift is added to the collection on each additional day, and then
# the complete collection is sent. The first three verses of the song are shown below.
# The complete lyrics are available on the Internet.
#
#   On the first day of Christmas
#   my true love sent to me:
#   A partridge in a pear tree.
#   On the second day of Christmas
#   my true love sent to me:
#   Two turtle doves,
#   And a partridge in a pear tree.
#   On the third day of Christmas
#   my true love sent to me:
#   Three French hens,
#   Two turtle doves,
#   And a partridge in a pear tree.
#
# Write a program that displays the complete lyrics for The Twelve Days of Christmas.
# Your program should include a function that displays one verse of the song. It
# will take the verse number as its only parameter. Then your program should call this
# function 12 times with integers that increase from 1 to 12.
# Each item that is sent to the recipient in the song should only appear in your
# program once, with the possible exception of the partridge. It may appear twice if
# that helps you handle the difference between “A partridge in a pear tree” in the first
# verse and “And a partridge in a pear tree” in the subsequent verses. Import your
# solution to Exercise 89 to help you complete this exercise.
#

from es89 import ordinal

# compute verses
def print_verse(num):
    
    if num == 1:
        verse = "A partridge in a pear tree"
    elif num == 2:
        verse = "Two turtle doves"
    elif num == 3:
        verse = "Three French hens"
    elif num == 4:
        verse = "Four calling birds"
    elif num == 5:
        verse = "Five gold rings"
    elif num == 6:
        verse = "Six geese a laying"
    elif num == 7:
        verse = "Seven swans a swimming"
    elif num == 8:
        verse = "Eight maids a milking"
    elif num == 9:
        verse = "Nine ladies dancing"
    elif num == 10:
        verse = "Ten lords a leaping"
    elif num == 11:
        verse = "Eleven pipers piping"
    elif num == 12:
        verse = "Twelve drummers drumming"

    return verse

def main():
    # set counter for manage first verse ("A partridge in a pear tree" / "And a partridge in a pear tree")
    strophe_counter = 1

    # print 12 strophes
    for num in range(1, 13):
        # set initial enumeration
        gifts = ""

        print("On the %s day of Christmas \nmy true love sent to me:" %ordinal(num))

        # compute progressive gifts enumeration 
        for num in range(1, num + 1):
            
            # manage the variation of first verse
            if num == 1 and strophe_counter != 1:
                gifts = print_verse(num) + "\n" + gifts
                gifts = "And a" + gifts[1:]
              
            else:
                gifts = print_verse(num) + "\n" + gifts

        # add counter strophe and print gifts        
        strophe_counter += 1
        print(gifts)
        print("")

    
if __name__ == "__main__":
    main()