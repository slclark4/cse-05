import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point
from game.scripting.move_actors_action import MoveActorsAction




class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, x, y, color):
        super().__init__()
        self._segments = []
        self._prepare_body(x, y, color)
        self._color = color


    def get_segments(self):
        return self._segments
    
    def execute(self, cast, script):
            cast = MoveActorsAction()

    def move_next(self):
    # move all segments
        
        for segment in self._segments:
            segment.move_next()
        self.grow_tail(2)


        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)



    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments ):
        
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self, x, y, bcolor):
        # x = int(constants.MAX_X / 2) 
        # y = int(constants.MAX_Y / 2) 

        for i in range(constants.SNAKE_LENGTH): 
            position = Point(x, y - i * constants.CELL_SIZE)
            velocity = Point(0, 1 * constants.CELL_SIZE)
            text = "8" if i == 0 else "#" 
            color = constants.YELLOW if i == 0 else bcolor

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color) 
            self._segments.append(segment)
        