from game.shared.constants import *
from .action import Action

class ActorOutputs(Action):
    """Display the actors in the screen
    
    The responsibility of ActorUpdates is to print the actors in the screen.
    """
    
    def __init__(self, video_service):
        """Constructs a new instance of ActorOutputs"""
        self._video_service = video_service
    
    def execute(self, cast, script):
        """Executes the actor updates
        
        Args:
        ---
            cast (Cast): The cast of actors.
            script (Script): The script of actions in the game
        """
        self._do_outputs(cast)
        
    def _do_outputs(self, cast):
        """A place to add the actor updates, like fire, move next, destroy, etc.
        
        Args:
        ---
            cast (Cast): The cast of actors
        """
        all_actors = cast.get_all_actors()
        self._video_service.clear_buffer()
        
        #NOTE: Add your actor drawings here
        self._video_service.draw_actors(all_actors)
        
        self._video_service.flush_buffer()