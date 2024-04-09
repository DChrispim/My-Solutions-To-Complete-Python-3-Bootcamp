import unittest
from spy_game import *

class TestSpyGame(unittest.TestCase):

    def test_original_1(self):
        result = spy_game([1,2,4,0,0,7,5,7])
        self.assertEqual(result, True)

    def test_original_2(self):
        result = spy_game([1,2,4,0,0,7,5])
        self.assertEqual(result, True)

    def test_original_3(self):
        result = spy_game([1,0,2,4,0,5,7])
        self.assertEqual(result, True)

    def test_original_4(self):
        result = spy_game([1,7,2,0,4,5,0])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
