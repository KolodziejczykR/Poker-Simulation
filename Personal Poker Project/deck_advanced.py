import random as r

def create_deck():
    """
    Creates a deck from scratch.
    Ace is defined as 1, Jack as 11, Queen as 12, and King as 13

    :param: None
    :return: A newly created deck of cards in a array
    """
    deck = []
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suits = ["Diamond", "Heart", "Spade", "Club"]
    for card in range(len(cards)):
        for suit in range(len(suits)):
            deck.append([cards[card], suits[suit]])
    return deck

def shuffle_deck(deck):
    """
    Shuffles the given deck

    :param: The deck we want to shuffle
    :return: The given deck now shuffled
    """
    return r.shuffle(deck)

def deal_card(deck):
    """
    Removes a card from a given deck
    
    :param: The deck from which to remove a card
    :return: The card which is removed
    """
    card_dealt = deck[0]
    deck.pop(0)
    return card_dealt
