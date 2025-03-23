
#helper script to calculate the perimiter and readious of a circle

import math

class Circle:
    """
    Class with methods to calculate perimeter and area of a circle based on input radius provided.
    """
    def __init__(self, radius):
        """
        Initialize a Circle object with the given radius.
        Parameters:
            radius (float or int): The radius of the circle.
        Raises:
            ValueError: If radius cannot be converted to a float.
        """
        self.radius = float(radius)
    
    def calculate_perimeter(self):
        """
        Calculate the perimeter of the circle (2πr - formula)
        Input parameter:radious: is the radius of the circle.
        Returns:
            float: The perimeter of the circle.
        """
        # Perimeter of a circle = 2πr
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        """
        Calculate the area of the circle (πr² - formula)
        Input parameter:radious: is the radius of the circle.
        Returns:
            float: The area of the circle.
        """
        # Area of a circle = πr²
        return math.pi * (self.radius ** 2)