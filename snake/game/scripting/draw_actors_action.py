from game.scripting.action import Action
from game.shared.point import Point 
import constants 

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("player_1_scores")
        score1.set_text(f"Player One: {score1._points}") 

        score2 = cast.get_first_actor("player_2_scores") 
        score2.set_text(f"Player Two: {score2._points}") # Set text "Player Two" on screen.
        score2.set_position(Point((constants.MAX_X - 200), 0)) # Set position for Player Two.

        snake = cast.get_first_actor("player_1")
        segments = snake.get_segments()
        
        snake2 = cast.get_first_actor("player_2")
        score2 = cast.get_first_actor("player_2_scores")
        segments2 = snake2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()