import card as c
import testing as test

HAND_SIZE = 5
FLUSH = "flush"
TWO_PAIR = "two pair"
ONE_PAIR = "one pair"
HIGH_CARD = "high card"
NO_PAIRS = "no pairs"

class PokerHand:

    def __init__(self, card_list = []):        
        self.__contents = list(card_list)


    def add_card(self, card):
        """
        Adding a given card to our hand

        :param self: The hand we already have
        :param card: The card object we want to add to our hand
        """
        if len(self.__contents) < HAND_SIZE:
            self.__contents.append(card)


    def __is_hand_flush(self):
        """
        Checking to see if the given hand is a flush or not.

        :param self: The hand we want to check for a flush
        :return: If the given hand is a flush or not
        """
        flush_length = 5

        hand_suits = []
        for card in self.__contents:
            hand_suits.append(c.Card.get_suit(card))

        if hand_suits.count(hand_suits[0]) == flush_length:
            return True 
        else:
            return False

    def get_pairs(self):
        """
        Gets the pairs within a given hand

        :param self: The hand we want to know the pairs of
        :return: A sorted list of the pairs in the given hand, or a 
        constant NO_PAIRS if there are no pairs within the hand
        """
        pairs_list = []
        pairs_list_sorted = []

        card_ranks = []
        for card in self.__contents:
            card_ranks.append(c.Card.get_rank(card))
        
        count_of_rank = card_ranks.count(card_ranks[0])
        count_of_rank_card = card_ranks[0]
        
        for current_card_rank in card_ranks:
            if count_of_rank == 2 and card_ranks.count(current_card_rank) == 3: 
                count_of_rank = 4
                pairs_list.append(count_of_rank_card)
                pairs_list.append(current_card_rank)

            elif count_of_rank == 3 and card_ranks.count(current_card_rank) == 2:
                count_of_rank = 4
                pairs_list.append(count_of_rank_card)
                pairs_list.append(current_card_rank)

            elif count_of_rank == 2 and card_ranks.count(current_card_rank) == 2: 
                if current_card_rank != count_of_rank_card: # Regular two pair
                    count_of_rank = 4
                    pairs_list.append(count_of_rank_card) 
                    pairs_list.append(current_card_rank)
                    
                    count_of_rank_card = current_card_rank

            elif card_ranks.count(current_card_rank) == 4: # Four of a kind case
                pairs_list.append(current_card_rank)
                pairs_list.append(current_card_rank)
                pairs_list_sorted = sorted(pairs_list)[::-1]
                return pairs_list_sorted

            elif count_of_rank < card_ranks.count(current_card_rank):
                count_of_rank = card_ranks.count(current_card_rank)
                count_of_rank_card = current_card_rank

        if count_of_rank == 4:
            pairs_list_sorted = sorted(pairs_list)[::-1]
            return pairs_list_sorted
        
        elif count_of_rank >= 2:
            pairs_list.append(count_of_rank_card)
            return pairs_list
        
        return NO_PAIRS


    def classifying_paired_hand(self):
        """
        Determines whether the given hand is a two pair, one pair, or just a high card hand
        For this project, those types of hands are considered "paired hands", unlike a flush

        :param self: The given hand we want to know the paired hand type of
        :return: The type of paired hand the given hand is, either a constant TWO_PAIR, ONE_PAIR, or HIGH_CARD
        """
        if self.get_pairs() == NO_PAIRS:
            return HIGH_CARD
        
        elif len(self.get_pairs()) == 2:
            return TWO_PAIR
        
        else:
            return ONE_PAIR
        
    
    def type_of_hand(self):
        """
        Classifies the type of the given hand

        :return: The type of the given hand, either a constant FLUSH 
        or the value assigned by classifying_paired_hands()
        """

        if self.__is_hand_flush():
            return FLUSH
        else:
            return self.classifying_paired_hand()


    def __compare_high_card_helper(self):
        """
        Creates the hands and sorts the ranks within the hand
        to be used for compare_high_card()

        :return: The ranks of the cards in the given hand, sorted 
        """
        hand_ranks = []
        for card in self.__contents:
            hand_ranks.append(c.Card.get_rank(card))
    
        hand_ranks_sorted = []
        for i in range(HAND_SIZE):
            hand_ranks_sorted.append(sorted(hand_ranks)[HAND_SIZE-(i+1)])
        
        return hand_ranks_sorted


    def compare_high_card(self, other):
        """
        Comparing the card ranks between 2 given cards

        :param self: The first hand to compare
        :param other: The second hand to compare
        :return: -1 if self is worth LESS than other, zero if they are worth the SAME,
        and 1 if self is worth MORE than other, when both self and other are being compared on their card ranks.
        """
        hand_one_ranks = self.__compare_high_card_helper()
        hand_two_ranks = other.__compare_high_card_helper()

        for card_index in range(HAND_SIZE):
            if hand_one_ranks[card_index] != hand_two_ranks[card_index]:
                if hand_one_ranks[card_index] > hand_two_ranks[card_index]:
                    return 1
                elif hand_two_ranks[card_index] > hand_one_ranks[card_index]:
                    return -1

        return 0

    def compare_pair_hands(self, other):
        """
        Comparing the strength of 2 given hands classified as either two pair or one pair hands

        :param self: The first hand to compare
        :param other: The second hand to compare
        :return: -1 if self is worth LESS than other, zero if they are worth the SAME,
        and 1 if self is worth MORE than other when both self and other are categorized as two pair or one pair hands.
        """
        if self.get_pairs() > other.get_pairs():
            return 1
        
        elif other.get_pairs() > self.get_pairs():
            return -1
        
        else:
            return self.compare_high_card(other)
        

    def compare_to(self, other):
        """
        Determines how this hand compares to another hand, returns 1, -1, or zero depending on the comparison.

        :param self: The first hand to compare
        :param other: The second hand to compare
        :return: -1 if self is worth LESS than other, zero if they are worth the SAME, and 1 if self is worth MORE than other.
        """
        self_hand_type = self.type_of_hand()
        other_hand_type = other.type_of_hand()

        if self_hand_type == FLUSH:
            if other_hand_type != FLUSH:
                return 1   
            
            else:
                return self.compare_high_card(other)
        
        elif self_hand_type == TWO_PAIR:
            if other_hand_type == FLUSH:
                return -1
            
            elif other_hand_type == TWO_PAIR:
                return self.compare_pair_hands(other)

            else:
                return 1
        
        elif self_hand_type == ONE_PAIR:
            if other_hand_type == FLUSH or other_hand_type == TWO_PAIR:
                return -1

            elif other_hand_type == ONE_PAIR:
                return self.compare_pair_hands(other)
            
            else:
                return 1
            
        elif self_hand_type == HIGH_CARD:
            if other_hand_type != HIGH_CARD:
                return -1
            
            else:
                return self.compare_high_card(other)
            

    def get_correct_reason(self, other):
        """
        Gets the correct reason for why one hand is better than another when comparing

        :param self: The first hand we are comparing
        :param other: The second hand we are comparing
        :return: The reason why one hand is better than the other in a string, depending on each hand
        """
        self_hand_type = self.type_of_hand()
        other_hand_type = other.type_of_hand()
        
        if self.compare_to(other) == 1:
            if self_hand_type == FLUSH:
                if other_hand_type == FLUSH:
                    return "Hand 1 wins on high card over Hand 2 since they are both flushes"
                else:
                    return ("Hand 1 is a flush while Hand 2 is a %s" % other_hand_type)

            elif self_hand_type == TWO_PAIR:
                if other_hand_type != TWO_PAIR:
                    return ("Hand 1 is a two pair while Hand 2 is a %s" % other_hand_type)
                else:
                    if self.compare_pair_hands(other) == 1:
                        return "Hand 1 has a better two pair than Hand 2"
                    else:
                        "Hand 1 wins on high card over Hand 2 since they have equal two pairs"
            
            elif self_hand_type == ONE_PAIR:
                if other_hand_type == ONE_PAIR:
                    if self.compare_pair_hands(other) == 1:
                        return "Hand 1 has a better one pair than Hand 2"
                    else:
                        return "Hand 1 wins on high card over Hand 2 since they have equal one pairs"
                else:
                    return "Hand 1 is a one pair while Hand 2 is a high card"

            else:
                return "Hand 1 wins on high card over Hand 2"
        
        elif self.compare_to(other) == -1:
            if other_hand_type == FLUSH:
                if self_hand_type == FLUSH:
                    return "Hand 2 wins on high card over Hand 1 since they are both flushes"
                else:
                    return ("Hand 2 is a flush while Hand 1 is a %s" % self_hand_type)
           
            elif other_hand_type == TWO_PAIR:
                if self_hand_type != TWO_PAIR:
                    return ("Hand 2 is a two pair while Hand 1 is a %s" % self_hand_type)
                else:
                    if self.compare_pair_hands(other) == -1:
                        return "Hand 2 has a better two pair than Hand 1"
                    else:
                        "Hand 2 wins on high card over Hand 1 since they have equal two pairs"
            
            elif other_hand_type == ONE_PAIR:
                if self_hand_type == ONE_PAIR:
                    if self.compare_pair_hands(other) == -1:
                        return "Hand 2 has a better one pair than Hand 1"
                    else:
                        return "Hand 2 wins on high card over Hand 1 since they have equal one pairs"
                else:
                    return "Hand 2 is a one pair while Hand 1 is a high card"

            else:
                return "Hand 2 wins on high card over Hand 1"

        else:
            return "Hand 1 and Hand 2 are equal with the same cards"

   
    def __str__(self):
        return str(self.__contents)
    
    def __repr__(self):
        return str(self)
    
    # allowing a PokerHand object to be iterable
    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        if self.__index < len(self.__contents):
            current_card = self.__contents[self.__index]
            self.__index += 1
            return current_card

        else:
            raise StopIteration


def __test_compare_to():
    """
    Have done more tests than this, only formatted to unit testing 
    after I did major testing and got 100% on gradescope tests
    """
    suite = test.TestSuite()

    suite.set_verbose(False) ## Show details of only failed tests.

    hand1 = PokerHand([c.Card(14, "Diamonds"), c.Card(8, "Hearts"), c.Card(8, "Diamonds"), c.Card(14, "Diamonds"), c.Card(5, "Diamonds")])
    hand2 = PokerHand([c.Card(6, "Spades"), c.Card(8, "Hearts"), c.Card(8, "Diamonds"), c.Card(14, "Spades"), c.Card(14, "Spades")])
    hand3 = PokerHand([c.Card(6, "Spades"), c.Card(8, "Hearts"), c.Card(8, "Diamonds"), c.Card(8, "Spades"), c.Card(4, "Spades")])
    hand4 = PokerHand([c.Card(12, "Spades"), c.Card(5, "Hearts"), c.Card(5, "Diamonds"), c.Card(9, "Spades"), c.Card(9, "Spades")])
    hand5 = PokerHand([c.Card(6, "Spades"), c.Card(8, "Spades"), c.Card(7, "Spades"), c.Card(14, "Spades"), c.Card(12, "Spades")])
    hand6 = PokerHand([c.Card(2, "Spades"), c.Card(5, "Spades"), c.Card(4, "Spades"), c.Card(13, "Spades"), c.Card(10, "Spades")])
    hand7 = PokerHand([c.Card(14, "Spades"), c.Card(13, "Hearts"), c.Card(12, "Diamonds"), c.Card(11, "Spades"), c.Card(9, "Spades")])
    hand8 = PokerHand([c.Card(14, "Hearts"), c.Card(13, "Diamonds"), c.Card(12, "Spades"), c.Card(11, "Clubs"), c.Card(10, "Clubs")])
    hand9 = PokerHand([c.Card(14, "Hearts"), c.Card(13, "Diamonds"), c.Card(12, "Spades"), c.Card(11, "Clubs"), c.Card(9, "Clubs")])
    hand10 = PokerHand([c.Card(14, "Spades"), c.Card(14, "Clubs"), c.Card(12, "Clubs"), c.Card(8, "Spades"), c.Card(9, "Diamonds")])
    hand11 = PokerHand([c.Card(14, "Hearts"), c.Card(14, "Diamonds"), c.Card(12, "Spades"), c.Card(8, "Clubs"), c.Card(9, "Clubs")])
    hand12 = PokerHand([c.Card(14, "Hearts"), c.Card(14, "Diamonds"), c.Card(12, "Spades"), c.Card(7, "Clubs"), c.Card(9, "Clubs")])
    hand13 = PokerHand([c.Card(14, "Hearts"), c.Card(14, "Diamonds"), c.Card(12, "Spades"), c.Card(12, "Clubs"), c.Card(12, "Diamonds")])
    hand14 = PokerHand([c.Card(12, "Hearts"), c.Card(12, "Diamonds"), c.Card(12, "Spades"), c.Card(14, "Clubs"), c.Card(14, "Diamonds")])
    hand15 = PokerHand([c.Card(14, "Hearts"), c.Card(14, "Diamonds"), c.Card(11, "Spades"), c.Card(12, "Clubs"), c.Card(12, "Diamonds")])
    hand16 = PokerHand([c.Card(12, "Hearts"), c.Card(12, "Diamonds"), c.Card(12, "Spades"), c.Card(14, "Clubs"), c.Card(14, "Diamonds")])
    hand17 = PokerHand([c.Card(12, "Hearts"), c.Card(12, "Diamonds"), c.Card(9, "Spades"), c.Card(9, "Clubs"), c.Card(9, "Diamonds")])
    hand18 = PokerHand([c.Card(12, "Hearts"), c.Card(12, "Diamonds"), c.Card(9, "Spades"), c.Card(9, "Clubs"), c.Card(9, "Diamonds")])
    hand19 = PokerHand([c.Card(14, "Spades"), c.Card(14, "Hearts"), c.Card(12, "Diamonds"), c.Card(11, "Spades"), c.Card(9, "Spades")])
    hand20 = PokerHand([c.Card(14, "Hearts"), c.Card(14, "Diamonds"), c.Card(12, "Spades"), c.Card(11, "Clubs"), c.Card(10, "Clubs")])
    hand21 = PokerHand([c.Card(12, "Hearts"), c.Card(12, "Diamonds"), c.Card(12, "Spades"), c.Card(12, "Clubs"), c.Card(4, "Clubs")])
    hand22 = PokerHand([c.Card(12, "Hearts"), c.Card(12, "Diamonds"), c.Card(10, "Spades"), c.Card(10, "Clubs"), c.Card(8, "Clubs")])


    suite.assert_equals("testing for high card in equal two pairs", hand1.compare_to(hand2), -1)
    suite.assert_equals("trips versus two pair", hand3.compare_to(hand4), -1)
    suite.assert_equals("high card flushes", hand5.compare_to(hand6), 1)
    suite.assert_equals("high card tie x4", hand7.compare_to(hand8), -1)
    suite.assert_equals("flush vs two pair", hand1.compare_to(hand6), -1)
    suite.assert_equals("high card true tie", hand7.compare_to(hand9), 0)
    suite.assert_equals("one pair true tie", hand10.compare_to(hand11), 0)
    suite.assert_equals("one pair last high card", hand10.compare_to(hand12), 1)
    suite.assert_equals("full house tie", hand13.compare_to(hand14), 0)
    suite.assert_equals("two pair high card", hand15.compare_to(hand16), -1)
    suite.assert_equals("full house tie 2", hand14.compare_to(hand16), 0)
    suite.assert_equals("full house tie 3 (same hand)", hand17.compare_to(hand18), 0)
    suite.assert_equals("two pair vs one pair", hand4.compare_to(hand10), 1)
    suite.assert_equals("one pair last high card", hand19.compare_to(hand20), -1)
    suite.assert_equals("full house vs two pair", hand17.compare_to(hand1), -1)
    suite.assert_equals("quads vs two pair", hand21.compare_to(hand22), 1)
    suite.assert_equals("same hand (one pair)", hand20.compare_to(hand20), 0)
    
    suite.print_summary()

if __name__ == "__main__":
    # tests
    __test_compare_to()
