from game.scripting.action import Action
from game.services.keyboard_service import KeyboardService


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def __init__(self):
        """"""
        self._keyboard_service = KeyboardService()
        self.game_started = False

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            if self.game_started == True:
                actor.move_next()
            else:
                if self._keyboard_service.is_key_down('a'):
                    self.game_started = True

                    # right
                if self._keyboard_service.is_key_down('d'):
                    self.game_started = True

                    # up
                if self._keyboard_service.is_key_down('w'):
                    self.game_started = True

                    # down
                if self._keyboard_service.is_key_down('s'):
                    self.game_started = True

                if self._keyboard_service.is_key_down('i'):
                    self.game_started = True

                    # right
                if self._keyboard_service.is_key_down('l'):
                    self.game_started = True

                    # up
                if self._keyboard_service.is_key_down('k'):
                    self.game_started = True

                    # down
                if self._keyboard_service.is_key_down('j'):
                    self.game_started = True