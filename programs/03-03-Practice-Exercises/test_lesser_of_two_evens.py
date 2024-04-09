import unittest
from lesser_of_two_evens import *

class TestLesserOfTwoEvens(unittest.TestCase):
    def test_all_even(self):
        result = lesser_of_two_evens(2, 4, 6, 8, 10)
        self.assertEqual(result, 2)

    def test_all_odd(self):
        result = lesser_of_two_evens(1, 3, 5, 7, 9)
        self.assertEqual(result, 9)

    def test_mixed_numbers(self):
        result = lesser_of_two_evens(1, 4, 7, 8, 10)
        self.assertEqual(result, 10)

    def test_single_number(self):
        result = lesser_of_two_evens(3)
        self.assertEqual(result, 3)

    def test_original_1(self):
        result = lesser_of_two_evens(2,4)
        self.assertEqual(result, 2)

    def test_original_2(self):
        result = lesser_of_two_evens(2,5)
        self.assertEqual(result, 5)

    def test_original_3(self):
        result = lesser_of_two_evens(3,7)
        self.assertEqual(result, 7)

if __name__ == '__main__':
    unittest.main()
