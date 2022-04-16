import pyray
import pathlib
from game.shared.constants import *

class AudioService:
    """This class in in charge of the game sounds/audio.
    The responsibility of AudioService is to play, stop, loop the audio sources as requested.
    """
    
    def __init__(self):
        """Constructs a new Audio Service"""
        self._sounds = {}
         
    def initialize(self):
        """Initializes the pyray audio service"""
        pyray.init_audio_device()
        
    def release(self):
        """Stops the audio device"""
        pyray.close_audio_device()
        
    def load_sounds(self):
        """Load all the audios defined in the audio constant"""
        sounds_dict = dict(zip(SOUNDS, SOUNDS))
        self._sounds = [(key, pyray.load_sound(str(pathlib.Path(value)))) for key,value in sounds_dict]
        
    def play_sound(self, sound):
        """Plays a loaded sound
        Args:
        ---
            sound (string): The location of the sound, this is the same as the key in the loaded sounds
        """
        pyray.set_sound_volume(self._sounds[sound.get_filename()], sound.get_volume())
        pyray.play_sound(self._sounds[sound.get_filename()])
        
    def is_sound_playing(self, sound):
        """Check if the audio is playing or not
        Args:
        ---
            sound (string): The location of the sound, this is the same as the key in the loaded sounds
        
        Returns:
        ---
            isPlaying (bool): True if the sound is being played, otherwhise False
        """
        isPlaying = pyray.is_sound_playing(self._sounds[sound.get_filename()])
        return isPlaying