from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
MAX_DISTANCE = 280


# TODO 1: Create Player class
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("purple")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # TODO 2: Create Movement methods
    def move_right(self):
        # MOVE RIGHT
        if self.xcor() < MAX_DISTANCE:
            self.goto((self.xcor() + MOVE_DISTANCE, self.ycor()))

    def move_left(self):
        # MOVE LEFT
        if self.xcor() > -MAX_DISTANCE:
            self.goto((self.xcor() - MOVE_DISTANCE, self.ycor()))

    def move_up(self):
        # MOVE UP
        if self.ycor() < MAX_DISTANCE:
            self.goto((self.xcor(), self.ycor() + MOVE_DISTANCE))

    def move_down(self):
        # MOVE DOWN
        if self.ycor() > -MAX_DISTANCE:
            self.goto((self.xcor(), self.ycor() - MOVE_DISTANCE))

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def in_finish_line(self):
        if self.ycor() > 270:
            return True
        else:
            return False
