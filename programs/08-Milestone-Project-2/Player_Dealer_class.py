# imports
from Deck_class import *

class Hand:
    def __init__(self):
        self.cards = [] 
        self.value = 0 
        # attribute to keep track of number of aces
        self.aces = 0 

    def add_cards(self, card):
        self.value += values[card.rank]
        self.cards.append(card)
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def show_hand(self, all_cards = True):
        if all_cards:
            card_list = [str(card) for card in self.cards]
            return f"The Player has in the hand {', '.join(card_list)} with a total value of {self.value}."
        else:
            card_list = [str(card) for card in self.cards][1:]
            card_value = sum([values[card.rank] for card in self.cards][1:])
            return f"The Dealer has the faceup cards {', '.join(card_list)} (value {card_value}) and a hidden card."

    def clear_hand(self):
        self.cards = []
        self.value = 0
        self.aces = 0

class Player(Hand):
    def __init__(self, total_chips=100):
        super().__init__()
        self.total_chips = total_chips
        self.current_bet = 0

    def bet(self, value_of_bet):
        self.current_bet = value_of_bet

    def win_bet(self):
        self.total_chips += 2  *self.current_bet
        self.current_bet = 0

    def lose_bet(self):
        self.total_chips -= self.current_bet
        self.current_bet = 0

    def show_chips(self):
        return f"The Player has {self.total_chips} chips"

class Dealer(Hand):
    def __init__(self):
        super().__init__()

    def __str__(self):
        card_list = [str(card) for card in self.cards]
        return f"The Dealer has in the hand {card_list} with sums {self.value}"
