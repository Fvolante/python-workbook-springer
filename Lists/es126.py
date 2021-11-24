## 
# In many card games each player is dealt a specific number of cards after the deck
# has been shuffled. Write a function, deal, which takes the number of hands, the
# number of cards per hand, and a deck of cards as its three parameters. Your function
# should return a list containing all of the hands that were dealt. Each hand will be
# represented as a list of cards.
# When dealing the hands, your function should modify the deck of cards passed
# to it as a parameter, removing each card from the deck as it is added to a player’s
# hand. When cards are dealt, it is customary to give each player a card before any
# player receives an additional card. Your function should follow this custom when
# constructing the hands for the players.
# Use your solution to Exercise 125 to help you construct a main program that
# creates and shuffles a deck of cards, and then deals out four hands of five cards each.
# Display all of the hands of cards, along with the cards remaining in the deck after
# the hands have been dealt.

from es125 import createDeck, shuffle

""" 
deals a desidered amount of cards and hands from a deck
@params: list: a deck of cards, int: number of hands, int: number of cards per hand
@return: a list which contains one list of cards per hand
"""
def deal(deck, number_of_hands, cards_per_hand):

    # create result list and populate it with exact amount of hands lists
    result = []
    for i in range(number_of_hands):

        result.append([])

    # loop until cards per hand are dealed and populate each hand removing from initial deck
    cards_dealed = 0

    while cards_dealed < cards_per_hand:

        for hand in result:

            # stop if initial deck doesn't contains cards
            if not deck:
                break

            card = deck.pop()
            hand.append(card)

        cards_dealed += 1

    return result

def main():

    # create and shuffle deck
    deck = shuffle( createDeck() )

    # deal cards
    print( "The hands are:\n", deal(deck, 4, 5) )
    print("The remaining cards are:\n", deck)

main()






