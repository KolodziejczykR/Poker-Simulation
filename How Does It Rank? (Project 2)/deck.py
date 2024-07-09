import random as r
import card as c

RANKS = c.RANKS
SUITS = c.SUITS

class Deck:
    
    def __init__(self):
        
        self.__deck_contents = []

        for rank in RANKS:
            for suit in SUITS:
                card = c.Card(rank, suit)
                self.__deck_contents.append(card)

    def shuffle_deck(self):
        """
        Shuffles the given deck
        
        :param self: The deck we want to shuffle
        :return: None, shuffles the already created deck
        """
        return r.shuffle(self.__deck_contents)

    def size(self):
        """
        :param self: The deck we want the length of
        :return: The length of the given deck
        """
        return len(self.__deck_contents)

    def deal_card(self):
        """
        Removes a card from a given deck when the deck is not empty
        
        :param self: The deck we want to remove the card from
        :return: The card which is removed
        """     
        return self.__deck_contents.pop(0) 
        
    def __str__(self):
        return str(self.__deck_contents)
    
    def __repr__(self):
        return str(self)
    

if __name__ == "__main__":
    # tests
    deck = Deck()

    print(deck)
    print("\n")
    print(deck.deal_card())
