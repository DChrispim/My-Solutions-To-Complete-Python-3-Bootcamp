import unittest
from up_low_letter_counter import *

class TestUpLow(unittest.TestCase):
    def test_up_low_phrase(self):
        phrase = 'Hello Mr. Rogers, how are you this fine Tuesday?'
        result_phrase = up_low(phrase)
        expected_phase = '\n            Original String: Hello Mr. Rogers, how are you this fine Tuesday?\n            No. of Upper case characters: 4\n            No. of Lower case Characters: 33\n            '
        self.assertTrue(expected_phase in result_phrase)

if __name__ == '__main__':
    unittest.main()
