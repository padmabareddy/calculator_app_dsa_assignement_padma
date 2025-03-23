import unittest
import math
from circle import Circle

class TestCircle(unittest.TestCase):
    
    def test_calculate_perimeter(self):
        """Test the calculate_perimeter method of the Circle class."""
        # Create a circle with radius 5
        circle = Circle(5)
        expected_perimeter = 2 * math.pi * 5
        self.assertAlmostEqual(circle.calculate_perimeter(), expected_perimeter)
        
    def test_calculate_area(self):
        """Test the calculate_area method of the Circle class."""
        # Create a circle with radius 5
        circle = Circle(5)
        expected_area = math.pi * (5 ** 2)
        self.assertAlmostEqual(circle.calculate_area(), expected_area)

        # Test with radius = 0
        circle = Circle(0)
        self.assertAlmostEqual(circle.calculate_area(), 0)

if __name__ == "__main__":
    unittest.main()