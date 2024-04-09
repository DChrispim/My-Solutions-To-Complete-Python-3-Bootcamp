import unittest
from unique_elements import *

class TestUniqueElements(unittest.TestCase):
    def test_unique_1(self):
        result = unique_elements([1])
        self.assertTrue(result == [1])

    def test_unique_2(self):
        result = unique_elements([1,1,1,1,3,4,6,8,1])
        self.assertTrue(result == [1,3,4,6,8])

if __name__ == '__main__':
    unittest.main()
