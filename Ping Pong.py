from turtle import Turtle, Screen
import random
import time

# Constants
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
POSITIONS = ((0, 315), (0, 285), (0, 0))
BALL_HEADING = [10, 170, 350, 190]

# Paddle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("blue")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=6)
        self.goto(position)

    def move_up(self):
        if self.ycor() <= 265:
            self.forward(55)

    def move_down(self):
        if self.ycor() >= -265:
            self.backward(55)

# Ball

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=1, outline=1.5)
        self.setheading(random.choice(BALL_HEADING))
        self.speed("normal")

    def bouncing_from_side_walls(self):
        heading = self.heading()
        self.setheading(360 - heading)
        self.forward(60)

    def bouncing_from_paddle(self):
        heading = self.heading()
        self.setheading(170 - heading)
        self.forward(60)

# Score

class Score(Turtle):

    def __init__(self, position, score_1, score_2):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score1 = score_1
        self.score2 = score_2
        self.goto(position)

    def displaying_and_updating_score(self):
        self.write(f"{self.score1} : {self.score2}", False, "center", ("Arial", 20, "bold"))

    def score_title(self):
        self.write("Score", True, "center", ("Arial", 20, "bold"))

    def updating_score(self, ball, paddle_right, paddle_left):
        ball.reset()
        paddle_right.reset()
        paddle_left.reset()
        self.reset()
        self.displaying_and_updating_score()

    def final_score(self):
        self.write(f"Final Score \n\n        {self.score1} : {self.score2}", False, "center", ("Arial", 20, "bold"))

# Outline

class Decorate(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.pensize(2)
        self.hideturtle()
        self.penup()
        self.goto(-590, -345)
        self.pendown()
        self.setheading(90)
        self.goto(590, -345)
        self.goto(590, 345)
        self.goto(-590, 345)
        self.goto(-590, -345)

# Working

screen = Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.tracer(0)
score_main = Score(POSITIONS[0], PLAYER_1_SCORE, PLAYER_2_SCORE)
score_main.color("red")
score_main.score_title()
a = Decorate()

time.sleep(1.5)

true_statement1 = True

while true_statement1:

    ball = Ball()
    paddle_right = Paddle((575, 0))
    paddle_left = Paddle((-580, 0))
    score2 = Score(POSITIONS[1], PLAYER_1_SCORE, PLAYER_2_SCORE)
    score2.displaying_and_updating_score()

    true_statement = True

    screen.listen()
    screen.onkey(paddle_right.move_up, "Up")
    screen.onkey(paddle_right.move_down, "Down")
    screen.onkey(paddle_left.move_up, "w")
    screen.onkey(paddle_left.move_down, "s")

    while true_statement:

        ball.forward(10)
        time.sleep(0.0008)
        screen.update()

        if paddle_right.distance(ball) <= 60.0:
            ball.bouncing_from_paddle()

        elif paddle_left.distance(ball) <= 60.0:
            ball.bouncing_from_paddle()

        elif ball.xcor() > 600:
            PLAYER_1_SCORE += 1
            score2.updating_score(ball, paddle_right, paddle_left)
            true_statement = False
            time.sleep(1)

        elif ball.xcor() < -600:
            PLAYER_2_SCORE += 1
            score2.updating_score(ball, paddle_right, paddle_left)
            true_statement = False
            time.sleep(1)

        if ball.ycor() >= 340 or ball.ycor() <= -340:
            ball.bouncing_from_side_walls()

        if PLAYER_1_SCORE == 10 or PLAYER_2_SCORE == 10:
            score_main.reset()
            final_score = Score(POSITIONS[2], PLAYER_1_SCORE, PLAYER_2_SCORE)
            final_score.color("red")
            final_score.final_score()
            true_statement1 = False


screen.exitonclick()
