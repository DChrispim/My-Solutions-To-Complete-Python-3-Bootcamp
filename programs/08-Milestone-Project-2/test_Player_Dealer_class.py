# imports
import unittest
from Player_Dealer_class import *
from Deck_class import *


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(total_chips=100)

    def test_win_bet(self):
        self.player.bet(20)
        self.player.win_bet()
        self.assertEqual(self.player.total_chips, 140)  # 100 + 2 * 20

    def test_lose_bet(self):
        self.player.bet(30)
        self.player.lose_bet()
        self.assertEqual(self.player.total_chips, 70)  # 100 - 30

    def test_str(self):
        self.assertEqual(str(self.player), "The Player has 100 chips")
        self.player.add_cards(Card("Hearts", "Ace"))
        self.assertEqual(str(self.player.show_hand()), "The Player has in the hand Ace of Hearts with a total value of 11.")
        
    

class TestHandOfPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(total_chips=100)

    def test_add_cards(self):
        self.player.add_cards(Card("Hearts", "Ace"))
        self.assertEqual(self.player.value, 11)
        self.assertEqual(len(self.player.cards), 1)

    def test_adjust_for_ace(self):
        self.player.add_cards(Card("Hearts", "Ace"))
        self.player.add_cards(Card("Diamonds", "Ten"))
        self.player.adjust_for_ace()
        self.assertEqual(self.player.value, 21)
        self.assertEqual(len(self.player.cards), 2)

    def test_clear_hand(self):
        self.player.add_cards(Card("Spades", "King"))
        self.player.clear_hand()
        self.assertEqual(len(self.player.cards), 0)
        self.assertEqual(self.player.value, 0)

class TestDealer(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer()

    def test_str(self):
        self.dealer.add_cards(Card("Hearts", "Ace"))
        self.assertEqual(str(self.dealer), "The Dealer has in the hand ['Ace of Hearts'] with sums 11")
        self.dealer.add_cards(Card("Diamonds", "Ten"))
        self.assertEqual(len(self.dealer.cards), 2)
        self.assertEqual(str(self.dealer.show_hand(False)), "The Dealer has the faceup cards Ten of Diamonds.")

class TestHandOfDealer(unittest.TestCase):
    def setUp(self):
        self.dealer = Dealer()

    def test_add_cards(self):
        self.dealer.add_cards(Card("Hearts", "Ace"))
        self.assertEqual(self.dealer.value, 11)
        self.assertEqual(len(self.dealer.cards), 1)

    def test_adjust_for_ace(self):
        self.dealer.add_cards(Card("Hearts", "Ace"))
        self.dealer.add_cards(Card("Diamonds", "Ten"))
        self.dealer.adjust_for_ace()
        self.assertEqual(self.dealer.value, 21)
        self.assertEqual(len(self.dealer.cards), 2)

    def test_clear_hand(self):
        self.dealer.add_cards(Card("Spades", "King"))
        self.dealer.clear_hand()
        self.assertEqual(len(self.dealer.cards), 0)
        self.assertEqual(self.dealer.value, 0)

if __name__ == "__main__":
    unittest.main()
