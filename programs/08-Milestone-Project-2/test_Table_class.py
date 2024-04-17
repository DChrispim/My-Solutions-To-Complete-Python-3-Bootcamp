# imports
import unittest
from unittest.mock import patch
from Table_class import *

class TestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table()

    def test_take_bet(self):
        with patch('builtins.input', return_value='50'):    
            # Test if the player's bet is correctly set
            self.table.player.total_chips = 100
            self.table.take_bet()
            self.assertEqual(self.table.player.current_bet, 50)  # User input is 50

    def test_ask_to_play(self):
        with patch('builtins.input', return_value='yes'):   
            # Test if the user input for playing is correctly processed
            self.assertTrue(self.table.ask_to_play())  # User input is 'Yes'

    def test_shuffle_deck(self):
        # Test if the deck is shuffled
        original_order = self.table.deck.all_cards[:]
        self.table.shuffle_deck()
        self.assertNotEqual(self.table.deck.all_cards, original_order)

    def test_deal_to_player(self):
        # Test if card are dealt to the player
        self.table.deal_to_player()
        self.assertEqual(len(self.table.player.cards), 1)

    def test_deal_to_dealer(self):
        # Test if card are dealt to the dealer
        self.table.deal_to_dealer()
        self.assertEqual(len(self.table.dealer.cards), 1)

    def test_player_wins(self):
        # Test if player wins are correctly processed
        bet = 30
        initial_chips = self.table.player.total_chips
        self.table.player.current_bet = bet
        self.table.player_wins()
        self.assertEqual(self.table.player.current_bet, 0)
        self.assertEqual(self.table.player.total_chips, initial_chips + 2 * bet)

    def test_player_loses(self):
        # Test if player losses are correctly processed
        bet = 30
        initial_chips = self.table.player.total_chips
        self.table.player.current_bet = bet
        self.table.player_loses()
        self.assertEqual(self.table.player.current_bet, 0)
        self.assertEqual(self.table.player.total_chips, initial_chips - bet)

if __name__ == '__main__':
    unittest.main()
