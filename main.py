import random 

## Global Variables

suits = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
ranks = ('Two' , 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True

## Class

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


# test_deck = Deck()
# test_deck.shuffle()

# # Test player
# test_player = Hand()
# pulled_card = test_deck.deal()
# print(pulled_card)
# test_player.add_card(pulled_card)
# print(test_player.value)

class Chips:

    def __init(self, total=100): #Default starting chip value of 100
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lost_bet(self):
        self.total -= self.bet

##### FUNCTIONS #################################

def take_bets(chips):

    while True:

        try:
            chips.bet = int(input("Please place a bet. "))
        except ValueError:
            print('Sorry please provide an integer number')
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips available! You have: {chips.total}")
            else:
                break

def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing # To control an upcomign while loop

    while True:
        x = input('Hit or Stand? Enter h or s: ') ## Hit/h to recieve a card Stand/s to want no more cards

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands. Dealer's Turn.")
            playing = False
        else:
            print('Sorry, Please enter h or s only!')
            continue

        break

#Function to display cards

def show_some(player, dealer):
    #Display only first card of dealer
    print("\n Dealer's Hand: ")
    print("Second card is hidden!")
    print(dealer.cards[0])

    #Display all of player's hand/cards.
    print("\n Players's Hand: ")


def show_all(player, dealer):

    #Show all the dealer's cards

    print("\n Dealers's Hand: ")
    for card in dealer.cards:
        print(card)
    # Sum and display value of picture cards (J + K == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")
    #Show all the player's cards
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Players's hand is: {player.value}")

## Function for end game scenarios

def player_busts(player, dealer, chips):
    print('PLAYER BUST!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUST!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()

def push(player, dealer, chips):
    print("Dealer and Player tie! PUSH")

################### GAME LOGIC #################

while True:
    # Opening statement
    print('Welcome to BLACKJACK')
    # Create and shuffle a deck, deal two cards to player and dealer
    deck = Deck()
    deck.shuffle()
    # Player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    #Dealer
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Chips to player default is 100
    player_chips = Chips()

    # Prompt player to place a bet
    take_bet(player_chips)

    # Show cards (Keep 2nd dealer card hidden)

    show_some(player_hand, dealer_hand)

    while playing: # Global variable playing = True

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
    
        # Show cards (Keep 2nd dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player exceeds 21, player_busts and break loop
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value <= 17:
            hit(deck, dealer_hand)
        
        # Show all cards
        show_all(player_hand, dealer_hand)

        # Winning Scenarios
        if dealer_hand.value >21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

