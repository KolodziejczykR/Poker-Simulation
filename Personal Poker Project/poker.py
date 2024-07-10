import deck_advanced as d
import hand_advanced as h

'''
Advanced Poker Project, with all hand types and taking user input on how many hands wanted to simulate

Author: Ryan Kolodziejczyk
'''

HAND_SIZE = h.HAND_SIZE
NUMBER_OF_ROWS = 10

def simulating_hands(number_of_hands):
    """
    Simulates the number of hands given as well as tracking the hand types within the simulation
    
    :param: The number of hands being played
    :return: The formatted version of the desired statistics, fit to model the headers
    """
    deck = d.create_deck()
    d.shuffle_deck(deck)

    countdown_number_of_hands = number_of_hands
    
    straight_flush_count = 0
    straight_count = 0
    flush_count = 0
    quads_count = 0
    full_house_count = 0
    trips_count = 0
    two_pair_count = 0
    one_pair_count = 0
    high_card_count = 0

    while countdown_number_of_hands > 0:
        if len(deck) < HAND_SIZE:
            deck = d.create_deck()
            d.shuffle_deck(deck)
        
        hand = h.create_hand(deck)
        hand_type = h.type_of_hand(hand)
        
        if hand_type == "high card":
            high_card_count += 1
        elif hand_type == "one pair":
            one_pair_count += 1
        elif hand_type == "two pair":
            two_pair_count += 1
        elif hand_type == "trips":
            trips_count += 1
        elif hand_type == "straight":
            straight_count += 1
        elif hand_type == "flush":
            flush_count += 1
        elif hand_type == "full house":
            full_house_count += 1
        elif hand_type == "quads":
            quads_count += 1
        else:
            straight_flush_count += 1
        
        countdown_number_of_hands -= 1

    number_of_hands_formatted = '{:,}'.format(number_of_hands) # Adding the commas to the number of hands value for the table

    print('{:>10}'.format(number_of_hands_formatted), '{:12d}'.format(high_card_count), '{:6.2f}'.format((high_card_count/number_of_hands)*100), 
          '{:9d}'.format(one_pair_count), '{:6.2f}'.format((one_pair_count/number_of_hands)*100), 
          '{:10d}'.format(two_pair_count), '{: 06.2f}'.format((two_pair_count/number_of_hands)*100), 
          '{:15d}'.format(trips_count), '{: 06.2f}'.format((trips_count/number_of_hands)*100),
          '{:12d}'.format(straight_count), '{: 06.2f}'.format((straight_count/number_of_hands)*100),
          '{:10d}'.format(flush_count), '{: 06.2f}'.format((flush_count/number_of_hands)*100),
          '{:14d}'.format(full_house_count), '{: 06.2f}'.format((full_house_count/number_of_hands)*100),
          '{:9d}'.format(quads_count), '{: 06.2f}'.format((quads_count/number_of_hands)*100),
          '{:23d}'.format(straight_flush_count))
    

def make_headers():
    """
    Creating the headers for the table

    :param: None
    :return: The printed row of headers for the table
    """
    print('{:>10}'.format('# of Hands'),  '{:>19}'.format('High Card    %  '), 
          '{:>16}'.format('Pairs    %  '), '{:>17}'.format('2 Pairs    %  '),
          '{:>22}'.format('3 of a Kind    %  '), '{:>19}'.format('Straights    %  '),
          '{:>17}'.format('Flushes    %  '), '{:>21}'.format('Full Houses    %  '),
          '{:>16}'.format('Quads    %  '), '{:>23}'.format('Straight Flush Count'))

def get_number_of_hands():
    """
    Gets input from the user to see how many hands to simulate

    :return: The user inputted number of hands
    """
    hands = (int)(input("How many hands would you like to simulate (as an integer): \n"))
    
    if hands < NUMBER_OF_ROWS:
        print("The simulated number must be at least %s!" % NUMBER_OF_ROWS)
        return "break"

    elif hands % NUMBER_OF_ROWS != 0:
        print("The simulated number must be a multiple of %s!" % NUMBER_OF_ROWS)
        return "break"

    return hands

def play_rounds(number_of_hands):
    """
    The function that outputs the table of values for all of the different desired simulated hand numbers

    :param: None
    :return: The table of desired values
    """
    if number_of_hands != "break":
        make_headers()

        for row in range(1,NUMBER_OF_ROWS + 1):
            hand_number = row * (int)(number_of_hands/NUMBER_OF_ROWS)
            simulating_hands(hand_number)

if __name__ == "__main__":
    play_rounds(get_number_of_hands())
