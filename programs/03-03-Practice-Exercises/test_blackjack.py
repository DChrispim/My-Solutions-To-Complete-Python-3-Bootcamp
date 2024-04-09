import unittest
from blackjack import *


class TestBlackjack(unittest.TestCase):

    def test_original_1(self):
        result = blackjack(5,6,7)
        self.assertEqual(result, 18)

    def test_original_2(self):
        result = blackjack(9,9,9)
        self.assertEqual(result, 'BUST')
    
    def test_original_3(self):
        result = blackjack(9,9,11)
        self.assertEqual(result, 19)

if __name__ == '__main__':
    unittest.main()
