import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
CHANCE = 6


# TODO 5: Create Player class
class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.chance = CHANCE

    def create_car(self):
        random_num = random.randint(1, self.chance)
        if random_num == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_y = random.randint(-250, 250)
            new_car.goto((320, new_y))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.chance > 2:
            self.chance -= 1
