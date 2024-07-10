import deck_advanced as d
import card_advanced as c

HAND_SIZE = 5

def create_hand(deck):
    """
    Creating a new hand consisting of the hand size number of cards

    :param: A given deck
    :return: Newly created hand from the given
    """
    hand = []
    for card in range(HAND_SIZE):
        hand.append(d.deal_card(deck))
    return hand

def is_hand_straight(hand):
    """
    Checking to see if the given hand is a straight or not.

    :param: A hand we want to check for a straight
    :return: A boolean, true if the given hand is a straight and false if the hand is not a straight
    """
    card_ranks = []
    for card in hand:
        card_ranks.append(c.get_card_rank(card))

    card_ranks.sort()

    if card_ranks[0]+1 == card_ranks[1]:
        if card_ranks[1]+1 == card_ranks[2]:
            if card_ranks[2]+1 == card_ranks[3]:
                if card_ranks[3]+1 == card_ranks[4]:
                    return True

    # The straight with the ace being the high card for ten, jack, queen, king, ace
    elif card_ranks[0] == 1:
        if card_ranks[1] == 10:
            if card_ranks[2] == 11:
                if card_ranks[3] == 12:
                    if card_ranks[4] == 13:
                        return True

    else:
        return False

                    
def is_hand_flush(hand):
    """
    Checking to see if the given hand is a flush or not.

    :param: An array hand we want to check for a flush
    :return: If the given hand is a flush or not
    """
    flush_length = 5

    hand_suits = []
    for card in hand:
        hand_suits.append(c.get_card_suit(card))

    if hand_suits.count(hand_suits[0]) == flush_length:
        return True 
    else:
        return False

def is_hand_straight_flush(hand):
    """
    Checking to see if the given hand is a straight flush or not

    :param: A hand we want to check for a straight flush
    :return: If the given hand is a straight flush or not
    """
    if is_hand_flush(hand) and is_hand_straight(hand):
        return True
    
    return False

def classifying_paired_hands(hand):
    """
    Determines whether the given hand is a full house, quads, trips, two pair, a pair, or just a high card hand
    These types of hands are considered "paired hands", unlike a straight or flush
    
    :param: The given hand as an array we want to know the paired hand type of
    :return: The type of paired hand the given hand is as a string
    """
    card_ranks = []
    for card in hand:
        card_ranks.append(c.get_card_rank(card))

    # setting the count of rank and the card to the first card in the hand, before comparing through the loop
    highest_count_of_rank = card_ranks.count(card_ranks[0])
    card_of_highest_count = card_ranks[0]
    
    for current_card in card_ranks:
        if highest_count_of_rank == 2 and card_ranks.count(current_card) == 2:
            if current_card != card_of_highest_count: # checking for 2 pair, making count_of_rank 2.1 because 2, 3, and 4 are used already
                highest_count_of_rank = 2.1
                card_of_highest_count = current_card

        # checking for full house
        elif highest_count_of_rank == 3 and card_ranks.count(current_card) == 2:
            highest_count_of_rank = 5

        elif highest_count_of_rank == 2 and card_ranks.count(current_card) == 3:
            highest_count_of_rank = 5

        
        elif highest_count_of_rank < card_ranks.count(current_card):
            card_of_highest_count = current_card
            highest_count_of_rank = card_ranks.count(current_card)

    if highest_count_of_rank == 1:
       return "high card"
    
    elif highest_count_of_rank == 2:
        return "one pair"

    elif highest_count_of_rank == 2.1:
        return "two pair"
    
    elif highest_count_of_rank == 3:
        return "trips"

    elif highest_count_of_rank == 5:
        return "full house"

    else:
        return "quads"

    
def type_of_hand(hand):
    """
    Classifies the type of the given hand

    :param: The hand we want to know the type of
    :return: The type of the given hand
    """
    if is_hand_straight_flush(hand):
        return "straight flush"
    elif is_hand_straight(hand):
        return "straight"
    elif is_hand_flush(hand):
        return "flush"
    else:
        return classifying_paired_hands(hand)

if __name__ == "__main__":
    # tests
    start_deck = d.create_deck()
    hand = [start_deck[1], start_deck[5], start_deck[17], start_deck[13], start_deck[9]]
    print(hand)
    print(type_of_hand(hand))
    