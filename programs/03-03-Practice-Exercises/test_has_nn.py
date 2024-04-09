import unittest
from has_nn import *

class TestHasNN(unittest.TestCase):

    def test_original_1(self):
        result = has_nn([1, 3, 3], 3)
        self.assertEqual(result, True)

    def test_original_2(self):
        result = has_nn([1, 3, 1, 3], 3)
        self.assertEqual(result, False)

    def test_original_3(self):
        result = has_nn([3, 1, 3], 3)
        self.assertEqual(result, False)

    def test_1(self):
        result = has_nn([3, 1, 3, 1, 1], 1)
        self.assertEqual(result, True)

    def test_2(self):
        result = has_nn([3, 1, 3, 1, 1], 2)
        self.assertEqual(result, False)
    
    def test_3(self):
        result = has_nn([1, 1, 1, 2, 1, 2, 2], 2)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
