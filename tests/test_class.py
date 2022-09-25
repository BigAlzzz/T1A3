import pytest, blackjack

deck_ordered = """
Two of Hearts
Three of Hearts
Four of Hearts
Five of Hearts
Six of Hearts
Seven of Hearts
Eight of Hearts
Nine of Hearts
Ten of Hearts
Jack of Hearts
Queen of Hearts
King of Hearts
Ace of Hearts
Two of Diamonds
Three of Diamonds
Four of Diamonds
Five of Diamonds
Six of Diamonds
Seven of Diamonds
Eight of Diamonds
Nine of Diamonds
Ten of Diamonds
Jack of Diamonds
Queen of Diamonds
King of Diamonds
Ace of Diamonds
Two of Spades
Three of Spades
Four of Spades
Five of Spades
Six of Spades
Seven of Spades
Eight of Spades
Nine of Spades
Ten of Spades
Jack of Spades
Queen of Spades
King of Spades
Ace of Spades
Two of Clubs
Three of Clubs
Four of Clubs
Five of Clubs
Six of Clubs
Seven of Clubs
Eight of Clubs
Nine of Clubs
Ten of Clubs
Jack of Clubs
Queen of Clubs
King of Clubs
Ace of Clubs"""


# CARD
def test_card_string():
    card = blackjack.Card('Hearts', 'Two')
    assert card.__str__() == "Two of Hearts"

# # DECK
def test_deck_deal():
    deck_ordered = blackjack.Deck()
    # Check before shuffled
    pop = deck_ordered.deal()
    assert pop.__str__() == 'King of Clubs'


# def test_deck_shuffle():
    deck = blackjack.Deck()

    # Check before shuffled
    assert deck.__str__() == deck_ordered

    # Check after shuffled
    deck.shuffle()
    assert deck.__str__() != deck_ordered

