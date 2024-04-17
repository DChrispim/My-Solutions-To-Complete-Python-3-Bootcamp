# imports
import unittest
from Deck_class import *

class TestDeckAndCard(unittest.TestCase):
    def setUp(self):
        # Crie uma instância de Deck para usar nos testes
        self.deck = Deck()

    def test_deck_initialization(self):
        # Verifique se o deck foi inicializado corretamente
        self.assertEqual(len(self.deck.all_cards), 52)

    def test_deck_shuffle(self):
        # Verifique se o embaralhamento altera a ordem das cartas
        original_order = self.deck.all_cards[:]
        self.deck.shuffle()
        self.assertNotEqual(self.deck.all_cards, original_order)

    def test_deck_deal(self):
        # Verifique se a função deal remove uma carta do deck
        initial_length = len(self.deck.all_cards)
        self.deck.deal()
        self.assertEqual(len(self.deck.all_cards), initial_length - 1)

    def test_card_creation(self):
        # Verifique se a criação de uma carta funciona corretamente
        card = Card("Hearts", "A")
        self.assertEqual(card.suit, "Hearts")
        self.assertEqual(card.rank, "A")

if __name__ == "__main__":
    unittest.main()
