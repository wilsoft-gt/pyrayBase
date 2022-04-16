from game.shared.constants import *
from game.casting.sound import Sound

class Director:
    """A person who directs the game.
    
    The responsability of a Director is to control the sequence of play.
    
    Attributes:
    ---
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
        _audio_Service (AudioService): For providing sound
    """
    
    def __init__(self, keyboard_service, video_service, audio_service):
        """Constructs a new Director using the specified keyboard, video and audio services
        
        Args:
        ---
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            audio_service (AudioService): An instance of AudioService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._audio_Service = audio_service
        
    def start_game(self, cast, script):
        """Starts the game using the given cast. Runs the main game loop.
        
        Args:
        ---
            cast (Cast): The cast of actors
            script (Script): The script of actions in the game.
        """
        self._video_service.open_window()
        self._audio_Service.initialize()
        while self._video_service.is_window_open():
            self._execute_action("input", cast, script)
            self._execute_action("update", cast, script)
            self._execute_action("output", cast, script)
        self._video_service.close_window()
        
    def _execute_action(self, group, cast, script):
        """Calls the execute for each action in the given group.
        
        Args:
        ---
            gropus (string): The action group name.
            cast (Cast): The cast actors.
            script (Script): The script of actions
        """
        actions = script.get_actions(group)
        for action in actions:
            action.execute(cast,script)