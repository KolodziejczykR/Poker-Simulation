RANKS = [2,3,4,5,6,7,8,9,10,11,12,13,14]
SUITS = ["Diamonds", "Hearts", "Spades", "Clubs"]

class Card:

    def __init__(self, rank, suit):
        
        self.__rank = rank
        self.__suit = suit
        self.__card = [self.__rank, self.__suit]


    def get_rank(self):
        """
        :return: The rank of the given card
        """
        return self.__rank

    def get_suit(self):
        """
        :return: The suit of the given card
        """
        return self.__suit
    
    def get_rank_full_name(self):
        """
        Gets the full name of the rank for face cards and the aces

        :param self: The card we want the rank of
        :return: The full name of the rank for the given card
        """
        rank = self.get_rank()
        full_rank = ""
        
        if rank == 11:
            full_rank = "Jack"
        elif rank == 12:
            full_rank = "Queen"
        elif rank == 13:
            full_rank = "King"
        elif rank == 14:
            full_rank = "Ace"
        else:
            full_rank = rank

        return full_rank
    
    
    def get_suit_formatted_name(self):
        """
        Gets the formatted name of the suit for a given card

        :param self: The card we want the formatted suit of
        :return: The full formatted name of the given card for printing purposes
        """
        suit = self.get_suit()
        full_suit = ""

        if suit == "Diamonds":
            full_suit = " of Diamonds"
        elif suit == "Hearts":
            full_suit = " of Hearts"
        elif suit == "Spades": 
            full_suit = " of Spades"
        else:
            full_suit = " of Clubs"
        
        return full_suit
        

    def __str__(self):
        return str(self.__card)
    
    def __repr__(self):
        return str(self)
    