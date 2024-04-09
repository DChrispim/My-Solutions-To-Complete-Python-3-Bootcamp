
import unittest
from palindrome import *

class TestPalindrome(unittest.TestCase):
    def test_phrase_1(self):
        result = palindrome("nurses run")
        self.assertTrue(result)
    
    def test_phrase_2(self):
        result = palindrome('helleh')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
