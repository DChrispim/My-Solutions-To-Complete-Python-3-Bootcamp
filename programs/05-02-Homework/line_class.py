class Line:
    
    def __init__(self, coor1, coor2):
        """
        Initialize a Line object.

        param coor1: Position (tuple x1, y1) of the first point
        param coor2: Position (tuple x2, y2) of the second point
        """
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2
    
    def distance(self):
        """
        Calculate the distance between coor1 and coor2
        """
        return ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5
    
    def slope(self):
        """
        Calculate the slope of the line that connects coor1 and coor2
        """
        if self.x1 == self.x2:
            return float('inf')  # Vertical line
        return (self.y1 - self.y2) / (self.x1 - self.x2)
