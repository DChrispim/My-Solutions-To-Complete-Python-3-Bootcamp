import unittest
from yield_n_random import *

class TestYieldNRandom(unittest.TestCase):

    def test_yield_n_random(self):
        random.seed(0)
        result = []
        for n in yield_n_random(1,4,5):
            result.append(n)
        
        self.assertEqual(result, [4, 4, 1, 3, 4])

if __name__ == '__main__':
    unittest.main()
