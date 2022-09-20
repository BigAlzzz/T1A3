import random

suits = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
ranks = ('Two' , 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:

    def __init__(self):
        self.deck = [] # Empty list to start
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) # Adds card objecs to a list

    def __str__(self):
        deck_comp = '' #Empty list to start
        for card in self.deck:
            deck_comp += '\n '+ card.__str__() # Add Card Object's print string
        return "The deck has: " + deck_comp 
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards= [] # Empty list to start
        self.value = 0 # Zero value to start
        self.aces = 0 # Ace value tracker

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        #IF TOTAL VALUE > 21 AND there is an ACE
        # Change ace value to 1 instead of 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
class Chips:

    def __init__(self, total=100): #Default starting chip value of 100
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
