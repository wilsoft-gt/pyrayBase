from game.shared.constants import *
from .action import Action

class ActorInputs(Action):
    """Updates the actor instances
    
    The responsibility of ActorUpdates is to update the actor after
    performing the updates.
    """
    
    def __init__(self, keyboard_service, audo_service):
        """Constructs a new instance of ActorUpdates"""
        self._keyboard_service = keyboard_service
    
    def execute(self, cast, script):
        """Executes the actor updates
        
        Args:
        ---
            cast (Cast): The cast of actors.
            script (Script): The script of actions in the game
        """
        self._get_inputs(cast)
        
    def _get_inputs(self, cast):
        """A place to add the actor updates, like fire, move next, destroy, etc.
        
        Args:
        ---
            cast (Cast): The cast of actors
        """
        pass