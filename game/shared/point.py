from game.shared.constants import *
class Point:
    """A distance from a relative origin (0,0).
    
    The responsibility of Point is to hold and provide information about itself. Point has a few
    convenience methods for adding, scaling, and comparing them.
    
    Attributes:
    ---
        _x (integer): The horizontal distance from the origin
        _y (integer): The vertial distance from the origin
    """
    
    def __init__(self, x, y):
        """Counstructs a new Point using the specified x and y values
        
        Args:
        ---
            x (int): The specified x value
            y (int): The specified y value
        """
        
        self._x = x
        self._y = y
        
    def add(self, other):
        """Gets a new point that is the sum of this and the given one.
        
        Args:
        ---
            other (Point): The Point to add.
        Returns:
        ---
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return (Point(x,y))
        
    def equals(self, other):
        """Whether or not this Point is equal to the given one.
        
        Args:
        ---
            other (Point): The point to compare
        
        Returns:
        ---
            boolean: True if both x and y are equal; False if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()
        
        
    def gounding_equals(self, other):
        """Calculates if the other point is inside the bounding box of this point
        
        Args:
        ---
            other (Point): The other point to do the comparison
            
        Returns:
        ---
            boolean: True if other point is inside of this bounding box; False if otherwise
        """
        bounding_x = other.get_x() >= self._x and other.get_x() <= self._x + CELL_SIZE
        bounding_y = other.get_y() >= self._y and other.get_y() <= self._y + CELL_SIZE
        return bounding_x and bounding_y
        
    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
        ---
            integer: The horizontal distance
        """
        return self._x
        
    def get_x(self):
        """Gets the vertical distance.
        
        Returns:
        ---
            integer: The vertical distance
        """
        return self._y
        
    def scale(self, factor):
        """Scales the point by the provided factor
        
        Args:
        ---
            factor (int): The amount to scale
            
        Returns:
        ---
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)