import math

class Cylinder:

    def __init__(self, height=1, radius=1):
        """
        Initialize a Cylinder object.

        param height: Height of the cylinder (default is 1)
        param radius: Radius of the cylinder (default is 1)
        """
        self.height = height
        self.radius = radius

    def volume(self):
        """
        Calculate the volume of the cylinder.
        """
        return math.pi * self.height * self.radius ** 2

    def surface_area(self):
        """
        Calculate the surface area of the cylinder.
        """
        return 2 * math.pi * self.radius * (self.height + self.radius)
