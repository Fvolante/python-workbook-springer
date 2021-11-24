## 
# A standard deck of playing cards contains 52 cards. Each card has one of four suits
# along with a value. The suits are normally spades, hearts, diamonds and clubs while
# the values are 2 through 10, Jack, Queen, King and Ace.
# Each playing card can be represented using two characters. The first character is
# the value of the card, with the values 2 through 9 being represented directly. The
# characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack,
# Queen, King and Ace respectively. The second character is used to represent the suit
# of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for
# diamonds and “c” for clubs. The following table provides several examples of cards
# and their two-character representations.
#                   Card Abbreviation
#                   Jack of spades Js
#                   Two of clubs 2c
#                   Ten of diamonds Td
#                   Ace of hearts Ah
#                   Nine of spades 9s
# Begin by writing a function named createDeck. It will use loops to create a
# complete deck of cards by storing the two-character abbreviations for all 52 cards
# into a list. Return the list of cards as the function’s only result. Your function will
# not require any parameters.
# Write a second function named shuffle that randomizes the order of the cards
# in a list. One technique that can be used to shuffle the cards is to visit each element
# in the list and swap it with another random element in the list. You must write your
# own loop for shuffling the cards. You cannot make use of Python’s built-in shuffle
# function.
# Use both of the functions described in the previous paragraphs to create a main
# program that displays a deck of cards before and after it has been shuffled. Ensure
# that your main program only runs when your functions have not been imported into
# another file.

from random import randint

""" 
create a deck of cards
@params: none
@return: a list: elements are strings which rapresent a single card
"""
def createDeck():

    # set variables to create deck
    VALUES = [str(i) for i in range(2, 10)] + ["T", "J", "Q", "K", "A"]
    SUITS = ["s", "h", "d", "c"]
    deck = []

    # loop to create deck
    for suit in SUITS:

        for value in VALUES:

            deck.append(value + suit)

    return deck

""" 
shuffle the deck
@params: a list: a deck of cards
@return: a list: shuffled param list
"""
def shuffle(deck):
    
    # number of shuffles
    SHUFFLES = 1000
    
    for i in range(SHUFFLES):
        
        # pick random card
        card = deck.pop(randint(0, len(deck) - 1))
        
        # pick random position
        pos = randint(0, len(deck) - 1)

        # inserd card picked in position picked
        deck.insert(pos, card)

    return deck

def main():

    print("The decklist is:\n", createDeck())
    print("")
    print("The shuffled decklist is:\n", shuffle(createDeck()))

if __name__ == "__main__":
    main()
    




