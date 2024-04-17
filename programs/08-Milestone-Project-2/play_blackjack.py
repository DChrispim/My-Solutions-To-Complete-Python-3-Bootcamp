# imports
import os
from IPython.display import clear_output
from Player_Dealer_class import *
from Deck_class import *
from Table_class import *

def clear_screen():
    '''
    Function that clears the output, uses different function depending on the environment
    '''
    try:
        # Check if running in IPython environment
        ipython = get_ipython()
        if ipython is not None:
            # Execute in IPython environment
            clear_output(wait=True)
    except NameError:
        # Execute in Python terminal
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':

    clear_screen()
    
    # Game 
    
    # global variable
    playing = True

    # Intro message
    print("This is a game of Blackjack.")
    # Create table object
    table = Table()
    # Shuffle deck
    table.shuffle_deck()
    while playing:
        while True:
            # Ask the player if he is going to play
            if not table.ask_to_play():
                print("Bye bye! Thank you for playing!")
                playing = False
                break
            
            # Clear player and dealer hands
            table.player.clear_hand()
            table.dealer.clear_hand()

            # Clear terminal
            clear_screen()

            # Print player number of chips
            print(table.player.show_chips())

            table.take_bet()

            # Deal two cards to player
            table.deal_to_player()
            table.deal_to_player()

            # Deal two cards to dealer
            table.deal_to_dealer()
            table.deal_to_dealer()

            # Show all cards of player
            print(table.player.show_hand(all_cards = True))

            # Show cards of dealer (one is hidden)
            print(table.dealer.show_hand(all_cards = False))

            # Prompt for Player to Hit or Stand
            while True:
                player_input = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
                if player_input[0].lower() == 'h':
                    table.deal_to_player()
                    print("New hand of player:")
                    print(table.player.show_hand(all_cards = True))
                    if table.player.value > 21:
                        break

                elif player_input[0].lower() == 's':
                    print("Player stands. Dealer is playing.")
                    break

                else:
                    print("Sorry, please try again.")
                    continue
            

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if table.player.value > 21:
                print(f"Sorry! Player busted with {table.player.value}")
                table.player_loses()
            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        
            while table.dealer.value < 17:
                table.deal_to_dealer()

            # Show cards of dealer (one is hidden)
            print(table.dealer)

            # Run different winning scenarios

            if table.dealer.value > 21:
                print(f"Dealer busted! Player wins!")
                table.player_wins()

            elif table.dealer.value > table.player.value:
                print(f"Sorry! Dealer wins with {table.dealer.value}")
                table.player_loses()

            elif table.dealer.value < table.player.value:
                print(f"Player wins with {table.player.value}")
                table.player_wins()

            else:
                print(f"Dealer and player tie with {table.dealer.value}! PUSH!!")

            # Print player number of chips
            if table.player.total_chips == 0:
                print("Sorry! You lost all your chips. You can't play without chips.")
                playing = False
                break
            else:
                print(table.player.show_chips())
