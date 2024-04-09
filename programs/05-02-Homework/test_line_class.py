import unittest
from line_class import *

class TestLine(unittest.TestCase):

    def test_distance(self):
        line1 = Line((0, 0), (3, 4)) 
        self.assertAlmostEqual(line1.distance(), 5.0, places=6)

        line2 = Line((1, 1), (4, 5)) 
        self.assertAlmostEqual(line2.distance(), 5.0, places=6)

        line3 = Line((3, 2), (8, 10))
        self.assertAlmostEqual(line3.distance(), 9.4339811, places=6)

    def test_slope(self):
        line1 = Line((3, 2), (8, 10))
        self.assertEqual(line1.slope(), 1.6)

        line2 = Line((1, 1), (1, 4))
        self.assertEqual(line2.slope(), float('inf'))

        line3 = Line((0, 0), (1, 0))
        self.assertEqual(line3.slope(), 0)

if __name__ == '__main__':
    unittest.main()
