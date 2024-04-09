import unittest
from almost_there import *

class TestAlmostThereN(unittest.TestCase):

    def test_original_1(self):
        result = almost_there_n(90,2)
        self.assertEqual(result, True)
    
    def test_original_2(self):
        result = almost_there_n(104,2)
        self.assertEqual(result, True)
    
    def test_original_3(self):
        result = almost_there_n(150,2)
        self.assertEqual(result, False)
    
    def test_original_4(self):
        result = almost_there_n(209,2)
        self.assertEqual(result, True)

    def test_1(self):
        result = almost_there_n(209,3)
        self.assertEqual(result, True)

    def test_2(self):
        result = almost_there_n(309,3)
        self.assertEqual(result, True)

    def test_3(self):
        result = almost_there_n(409,3)
        self.assertEqual(result, False)

    def test_exception(self):
        with self.assertRaises(Exception) as context:
            almost_there_n(9,0)

        self.assertTrue("K must be greater than 1" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
