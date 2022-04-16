from game.shared.constants import *

from game.casting.cast import Cast

from game.directing.director import Director

from game.scripting.script import Script
from game.scripting.actor_inputs import ActorInputs
from game.scripting.actor_updates import ActorUpdates
from game.scripting.actor_outputs import ActorOutputs

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.audio_service import AudioService


def main():
    cast = Cast()
    #NOTE: Add all your actors here and add them to the cast instance
    
    keyboard_service = KeyboardService()
    video_service = VideoService()
    audio_service = AudioService()
    script = Script()
    
    script.add_action("input", ActorInputs(keyboard_service, audio_service))
    script.add_action("update", ActorUpdates())
    script.add_action("output", ActorOutputs(video_service))
    
    director = Director(keyboard_service, video_service, audio_service)
    director.start_game(cast, script)
    
if __name__ == "__main__":
    main()