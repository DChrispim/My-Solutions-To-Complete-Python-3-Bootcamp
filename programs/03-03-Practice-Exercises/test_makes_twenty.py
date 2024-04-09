import unittest
from makes_twenty import *

class TestMakesTwenty(unittest.TestCase):

    def test_original_1(self):
        result = makes_twenty(20,10)
        self.assertEqual(result, True)

    def test_original_2(self):
        result = makes_twenty(12,8)
        self.assertEqual(result, True)

    def test_original_3(self):
        result = makes_twenty(2,3)
        self.assertEqual(result, False)

    def test_n_numbers_1(self):
        result = makes_twenty(1,2,44,7,8,20,3)
        self.assertEqual(result, True)
    
    def test_n_numbers_2(self):
        result = makes_twenty(0)
        self.assertEqual(result, False)
    
    def test_n_numbers_3(self):
        result = makes_twenty(20)
        self.assertEqual(result, True)
        
    def test_n_numbers_4(self):
        result = makes_twenty(5,5,5,5)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
