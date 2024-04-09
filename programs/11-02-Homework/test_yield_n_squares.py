import unittest
from yield_n_squares import *

class TestYieldNSquares(unittest.TestCase):

    def test_yield_n_squares(self):
        result = []
        for n in yield_n_squares(5):
            result.append(n)
        
        self.assertEqual(result, [0,1,4,9,16,25])

if __name__ == '__main__':
    unittest.main()
