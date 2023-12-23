from turtle import Turtle
ALIGNMENT = "center"
FONT1 = ("Courier", 24, "normal")
FONT2 = ("Courier", 20, "bold")
FONT3 = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-210, 260)
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT1)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT1)
        self.goto(0, -50)
        self.write("Created by Alireza Mak.", align=ALIGNMENT, font=FONT2)
        self.goto(0, -100)
        self.write("Alirezamak.com", align=ALIGNMENT, font=FONT3)

    def next_level(self):
        self.clear()
        self.level += 1
        self.update_level()
