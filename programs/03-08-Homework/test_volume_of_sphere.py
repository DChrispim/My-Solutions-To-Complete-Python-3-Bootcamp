import unittest
from multiply import *

class TestMultiply(unittest.TestCase):
    def test_radius_1(self):
        result = multiply([1,2,3,-4])
        self.assertEqual(result, -24)  

if __name__ == '__main__':
    unittest.main()
