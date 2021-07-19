import time
import random
from turtle import Turtle, Screen

# Constants
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FONT = ('Courier', 24, 'normal')
car_list = []
LEVEL_SPEED = 0.1

# Player

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        new_ycor = self.ycor() + MOVE_DISTANCE
        new_xcor = self.xcor()
        self.goto(new_xcor, new_ycor)

# Cars

class CarManager(Turtle):

    starting_speed = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.goto(320, random.randint(-240, 250))
        self.speed_increase_var = CarManager.starting_speed

    def move_car(self):
        self.backward(CarManager.starting_speed)

    def speed_increase(self):
        CarManager.starting_speed += MOVE_INCREMENT

# Scoreboard

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.color("black")
        self.level = 1

    def displaying_level(self):
        self.write(f"Level {self.level}", False, "left", FONT)

    def updating_level(self):
        self.clear()
        self.level += 1
        self.displaying_level()

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", False, "left", FONT)

# Working

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
score.displaying_level()

screen.onkey(player.move, "Up")
screen.listen()

increase_car_speed = False

while_count = 0

game_is_on = True
while game_is_on:

    time.sleep(LEVEL_SPEED)
    screen.update()

    if while_count == 5:
        car = CarManager()
        car_list.append(car)
        while_count = 0

    for _ in car_list:
        _.move_car()

    if player.ycor() >= 290:
        player.goto(0, -280)
        car_list[0].speed_increase()
        score.updating_level()

    for _ in car_list:
        if _.distance(player) <= 20:
            score.game_over()
            game_is_on = False
        elif _.xcor() < -320:
            car_list.remove(_)

    while_count += 1

screen.exitonclick()
