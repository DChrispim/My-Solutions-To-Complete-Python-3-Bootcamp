import unittest
from count_primes import *

class TestCountPrimes(unittest.TestCase):

    def test_original_1(self):
        result = count_primes(10)
        self.assertEqual(result, 4)

    def test_original_2(self):
        result = count_primes(100)
        self.assertEqual(result, 25)

if __name__ == '__main__':
    unittest.main()
