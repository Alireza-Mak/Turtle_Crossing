import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# from car_manager import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# TODO 3: Instance of Player class
player = Player()

#  TODO 4: Listener for moving player
screen.listen()
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

# TODO 6: Instance of CarManager class
car_manager = CarManager()

# TODO 8: Instance of Scoreboard class
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # TODO 7: Find the collision
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
    # TODO 9: Level up
    if player.in_finish_line():
        player.go_to_start()
        scoreboard.next_level()
        car_manager.level_up()


screen.exitonclick()
