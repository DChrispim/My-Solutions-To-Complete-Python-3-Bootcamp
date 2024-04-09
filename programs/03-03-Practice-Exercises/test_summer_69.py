import unittest
from summer_69 import *

class TestSummer69(unittest.TestCase):

    def test_original_1(self):
        result = summer_69([1, 3, 5])
        self.assertEqual(result, 9)

    def test_original_2(self):
        result = summer_69([4, 5, 6, 7, 8, 9])
        self.assertEqual(result, 9)

    def test_original_3(self):
        result = summer_69([2, 1, 6, 9, 11])
        self.assertEqual(result, 14)

    def test_1(self):
        result = summer_69([])
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
