import blackjack, sys, clearing, colorama
from colorama import Fore
colorama.init(autoreset=True)

## Global Variables
playing = True

##### FUNCTIONS #################################

def take_bets(chips):

    while True:

        try:
            chips.bet = int(input("Please place a bet: "))
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
    global playing # To control while loop

    while True:
        x = input('\nHit or Stand? Enter h or s: ') ## Hit/h to recieve a card Stand/s to want no more cards

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
    print("\nDealer's Hand: ")
    print(dealer.cards[0])
    print("Second card is hidden!")
    

    #Display all of player's hand/cards.
    print("\nPlayers's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Players's hand is: {player.value}")


def show_all(player, dealer):

    #Show all the dealer's cards

    print("\nDealers's Hand: ")
    for card in dealer.cards:
        print(card)
    # Sum and display value of picture cards (J + K == 20)
    print(f"Value of Dealer's hand is: {dealer.value}")
    #Show all the player's cards
    print("\nPlayer's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Players's hand is: {player.value}")

## Function for end game scenarios

def player_busts(player, dealer, chips):
    print(Fore.RED + 'PLAYER BUST!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print(Fore.GREEN + 'PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print(Fore.GREEN + "PLAYER WINS! DEALER BUST!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print(Fore.RED + "Dealer Wins!")
    chips.lose_bet()

def push(player, dealer, chips):
    print(Fore.CYAN + "Dealer and Player tie! PUSH")

def clear():
    '''
    Clear the screen for better readability
    :return: None
    '''
    clearing.clear()

def show_rules():
    '''
    Print rules
    :return: None
    '''
    print("""
    The object of the game is to create card totals higher than those of the dealer's hand 
    but not exceeding 21, or by stopping at a total in the hope that dealer will bust.
    
    Number cards count as their numbers.
    Jack, Queen and King count as 10.
    Aces count as 1 or 11, acording to the players choice.
    
    After the player hits STAND the dealer's hand is resolved by 
    drawing cards until the hand achieves a total of 17 or higher.
    
    A player total of 21 on the first two cards is called Blackjack and the players wins
    immediatelly unless dealer has also one.
    """)

def welcome_screen():

    '''
    Print the welcome screen and ask user what he wants to do
    :return: None
    '''
    clear()
    print(Fore.MAGENTA +"""
        _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
                            / |                
                           /__/  
    \n
    Welcome to BlackJack!
    What do you want to do?
    [P]LAY
    [R]ULES
    [Q]UIT
    """
    )
    choice = str(input("Choice: \t"))
    while choice.lower() not in ['p', 'play', 'r', 'rules', 'q', 'quit']:
        choice = str(input("What do you want to do?\n"
                            "[P]LAY\n"
                            "[R]ULES\n"
                            "[Q]UIT\n"
                            "Choice: \t"))
    if choice.lower() in ['p', 'play']:
        main()
    elif choice.lower() in ['r', 'rules']:
        clear()
        show_rules()
        choice = str(input("Do you want to [P]LAY or [Q]UIT?\t"))
        while choice.lower() not in ['p', 'play', 'q', 'quit']:
            choice = str(input("Do you want to [P]LAY or [Q]UIT?\t"))
        if choice.lower() in ['p', 'play']:
            main()
        else:
            print("See you next time")
            sys.exit()
    else:
        print("Okay, maybe next time")
        sys.exit()

################### GAME LOGIC #################
player_chips = blackjack.Chips()
# playing = True
def main():
    global playing
    # Opening statement
    print('Welcome to BLACKJACK')
    print('You have a 100 chips to start with!')
    
    while True:
        # Create and shuffle a deck, deal two cards to player and dealer
        deck = blackjack.Deck()
        deck.shuffle()
        # Player
        player_hand = blackjack.Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        #Dealer
        dealer_hand = blackjack.Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())



        # Prompt player to place a bet
        take_bets(player_chips)

        # Show cards (Keep 2nd dealer card hidden)

        show_some(player_hand, dealer_hand)

        while playing: # Global variable playing = True

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)
        
            # Show cards (Keep 2nd dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player exceeds 21, player_busts and break loop
            if player_hand.value > 21:
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
                push(player_hand, dealer_hand, player_chips)
            
        # Display Player's chip total
        print(f"\nPlayer's total chips are : {player_chips.total}")

        #Do you want to play again
        new_game = input('Would you like to play another hand? (y/n)')

        if new_game[0].lower() == 'y':
            playing = True
            continue
        
        else:
            print('Thanks for playing!')
            break

    welcome_screen()

if __name__ == '__main__':
    welcome_screen()
