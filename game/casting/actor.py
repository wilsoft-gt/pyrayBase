from mimetypes import init
from shared.constants import *
from shared.color import Color
from shared.point import Point

class Actor:
    """A visible, moveable thing that participates in the game.
    
    The responsability of Actor is to keep track of its position and
    velocity in 2d space, this is a base class so other actor types can inherit.
    
    Attributes:
    ---
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
        _group (str): The group name of the actor.
        _score (int): The actor points (score).
    """
    
    def __init__(self):
        """Construct a new Actor."""
        self._position = Point(0,0)
        self._velocity = Point(0,0)
        self._group = ""
        self._points = 0
        
    def get_position(self):
        """Returns the actor position"""
        return self._position
        
    def get_velocity(self):
        """Returns the actor velocity"""
        return self._velocity
        
    def get_group(self):
        """Returns the actor group"""
        return self._group
        
    def get_points(self):
        """Returns the actor points"""
        return self._points
        
    def set_position(self, position):
        """Set the font position of the actor.
        
        Args:
        ---
            position (Point): The new actor position
        """
        self._position = position
        
    def set_velocity(self, velocity):
        """Set the velocity of the actor.
        
        Args:
        ---
            velocity (Point): The new actor velocity
        """
        self._velocity = velocity
        
    def set_group(self, group):
        """Set the group of the actor.
        
        Args:
        ---
            group (str): The new actor group
        """
        self._group = group
        
    def set_points(self, points):
        """Set the points of the actor.
        
        Args:
        ---
            points (int): The new actor points
        """
        self._points = points
        
    def move_next(self):
        """Moves the actor to its next position according to its
        velocity. WIll wrap the position from the one side of the
        screen to the other when it reaches the given maxium x and y values.
        
        Args:
        ---
            max_x (int): The maxium x value
            max_y (int): The maxium y value
        """
        x = (self._position.get_x() + self._velocity.get_x()) % MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % MAX_Y
        self._position = Point(x,y)