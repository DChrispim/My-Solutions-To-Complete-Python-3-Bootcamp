
import unittest
from ispangram import *

class TestIsPangram(unittest.TestCase):
    def test_phrase_1(self):
        result = ispangram("This is false")
        self.assertFalse(result)
    
    def test_phrase_2(self):
        result = ispangram("The quick brown fox jumps over the lazy dog")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
