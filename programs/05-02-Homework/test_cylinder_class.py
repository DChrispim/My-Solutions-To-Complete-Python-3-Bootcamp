
import unittest
from cylinder_class import *

class TestCylinder(unittest.TestCase):

    def test_volume(self):
        # Test with default values
        cylinder1 = Cylinder()
        self.assertAlmostEqual(cylinder1.volume(), math.pi)

        # Test with custom values
        cylinder2 = Cylinder(height=3, radius=2)
        self.assertAlmostEqual(cylinder2.volume(), 37.6991, 4)

    def test_surface_area(self):
        # Test with default values
        cylinder1 = Cylinder()
        self.assertAlmostEqual(cylinder1.surface_area(), 4 * math.pi)  # Surface area of a unit cylinder is 4pi

        # Test with custom values
        cylinder2 = Cylinder(height=3, radius=2)
        self.assertAlmostEqual(cylinder2.surface_area(), 62.8318, 3)  # Surface area of cylinder with height=3 and radius=2

if __name__ == '__main__':
    unittest.main()
