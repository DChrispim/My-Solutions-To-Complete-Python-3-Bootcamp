# imports
from Player_Dealer_class import *

class Table():
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()

    
    def take_bet(self):
        taking_bet = True
        while taking_bet:
            try:
                user_input = int(input("Please enter your bet: "))
                if user_input > self.player.total_chips:
                    print("You do not have enough chips!")
                elif user_input <= self.player.total_chips:
                    self.player.bet(user_input)
                    taking_bet = False
            except ValueError:
                print("Looks like you did not enter an integer!")
        print(f"Ok, your bet is {self.player.current_bet}")

    def ask_to_play(self):        
        play_game = input('Are you ready to play? Enter Yes or No.')
        return play_game.lower()[0] == 'y'

    def shuffle_deck(self):
        self.deck.shuffle()

    def deal_to_player(self):
        self.player.add_cards(self.deck.deal())
        self.player.adjust_for_ace()
    
    def deal_to_dealer(self):
        self.dealer.add_cards(self.deck.deal())
        self.dealer.adjust_for_ace()

    def show_table(self, all_cards = True):
        player.show_hand(all_cards)
        dealer.show_hand(all_cards)
    
    def player_wins(self):
        self.player.win_bet()
    
    def player_loses(self):
        self.player.lose_bet()
