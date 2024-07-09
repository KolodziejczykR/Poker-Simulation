import poker_hand as ph
import deck as d

HAND_SIZE = ph.HAND_SIZE

def __create_formatted_hands(deck, poker_hand):
    for i in range(HAND_SIZE):
            poker_hand.add_card(deck.deal_card())
    
    hand_formatted = []
    for card in poker_hand: # iterating through the Card objects that make up the given PokerHand object
        card_formatted = str(card.get_rank_full_name()) + card.get_suit_formatted_name()
        hand_formatted.append(card_formatted)
    
    return hand_formatted


def main():
    """
    Runs the game allowing the user to guess between 2 hands of which is stronger,
    giving the player points for every correct guess

    :return: None, prints when the player either guesses wrong or beats the deck, with their respective point total
    Also if the user guesses wrong, prints a reason for why the guess was wrong for those 2 specific hands
    """
    deck = d.Deck()
    deck.shuffle_deck()

    player_points = 0
    round = 1

    while deck.size() > HAND_SIZE*2:
        hand_one = ph.PokerHand()
        hand_two = ph.PokerHand()
         
        hand_one_formatted = __create_formatted_hands(deck, hand_one)
        hand_two_formatted = __create_formatted_hands(deck, hand_two)
        
        print("Round", round)
        print("Hand 1:")
        print(', '.join(hand_one_formatted))
       
        print("\nHand 2:")
        print(', '.join(hand_two_formatted))
        
        print("\nDo you think Hand 1 or Hand 2 is better, or are they equal?")
        user = int(input("Put 1 for Hand 1, 2 for Hand 2, or 0 for equal: "))

        if hand_one.compare_to(hand_two) == 1 and user == 1:
            player_points += 1
            print("\nNice job, you got it right! \n")
        
        elif hand_one.compare_to(hand_two) == -1 and user == 2:
            player_points += 1
            print("\nNice job, you got it right! \n")
        
        elif hand_one.compare_to(hand_two) == 0 and user == 0:
            player_points += 1
            print("\nNice job, you got it right! \n")
        
        else:
            print("\nSorry, you got this one wrong")
            print("The correct reasoning:", hand_one.get_correct_reason(hand_two), "\n")
            
            if player_points == 1:
                print("1 point")
            else:
                print("%d points" % player_points)  
            
            return
        
        round += 1

    print("Congratulations, you got the entire deck right. %s points!" % player_points)


if __name__ == "__main__":
    main()
