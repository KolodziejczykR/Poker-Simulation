import deck_advanced as d

def get_card_rank(card):
    """
    :return: The rank of the given card
    """
    return card[0]

def get_card_suit(card):
    """
    :return: The suit of the given card
    """
    return card[1]

if __name__ == "__main__":
    # tests
    deck = d.create_deck()
    d.shuffle_deck(deck)
    print(deck)
    for i in range(5):
        card = d.deal_card(deck)
        print(card)
        print(get_card_rank(card) + " of " + get_card_suit(card) + "s")
