from fileinput import filename

class Sound:
    """Create the qualities of audio
    
    The responsability of SOund is to get the filename, ,choose the volume and if the sound needs to repeat
    """
    
    def __init__(self, filepath, volume=1, repeat=False):
        """Construct a new sound using the specified filename, volume, and whether
        the sound should repeat.
        
        Args:
        ---
            filepath (string): gets the filepath of the sound
            volume (int): sets the volume for the audio
            repeat (bool): defines if the sound should keep playing or not
        """
        self._filename = filename
        self._volume = volume
        self._repeat = repeat
        
    def get_filename(self):
        """Returns the filename of the audio to play"""
        return self._filename
        
    def get_volume(self):
        """Return the audio volume"""
        return self._volume
        
    def get_repeat(self):
        """Return if audio should repeat or not"""
        return self._repeat
        
    def set_volume(self, volume):
        """Set the audio volume"""
        self._volume = volume
        
    def set_repeat(self, repeat):
        """Set if audio should repeat"""
        self._repeat = repeat