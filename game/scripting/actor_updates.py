from game.shared.constants import *
from .action import Action

class ActorUpdates(Action):
    """Updates the actor instances
    
    The responsibility of ActorUpdates is to update the actor after
    performing the updates.
    """
    
    def __init__(self):
        """Constructs a new instance of ActorUpdates"""
        pass
    
    def execute(self, cast, script):
        """Executes the actor updates
        
        Args:
        ---
            cast (Cast): The cast of actors.
            script (Script): The script of actions in the game
        """
        self._do_updates(cast)
        
    def _do_updates(self, cast):
        """A place to add the actor updates, like fire, move next, destroy, etc.
        
        Args:
        ---
            cast (Cast): The cast of actors
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()