import turtle
import time
import random

class SimpleSnakeGame:
    def __init__(self):
        self.delay = 0.1
        self.score = 0
        self.high_score = 0
        self.segments = []

        self.setup_screen()
        self.create_snake()
        self.create_food()
        self.create_pen()
        self.setup_controls()
        self.run_game()

    def setup_screen(self):
        self.wn = turtle.Screen()
        self.wn.title("Begineer Snake Game")
        self.wn.bgcolor("green")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0)  # Turns off the screen updates

    def create_snake(self):
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

    def create_food(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)

    def create_pen(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

    def setup_controls(self):
        self.wn.listen()
        self.wn.onkeypress(self.go_up, "w")
        self.wn.onkeypress(self.go_down, "s")
        self.wn.onkeypress(self.go_left, "a")
        self.wn.onkeypress(self.go_right, "d")

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + 20)

    def run_game(self):
        while True:
            self.wn.update()
            self.check_border_collision()
            self.check_food_collision()
            self.move_segments()
            self.move()
            self.check_self_collision()
            time.sleep(self.delay)

    def check_border_collision(self):
        if abs(self.head.xcor()) > 290 or abs(self.head.ycor()) > 290:
            self.reset_game()

    def check_food_collision(self):
        if self.head.distance(self.food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            self.food.goto(x, y)
            self.add_segment()
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            self.update_score_display()

    def add_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        self.segments.append(new_segment)
        self.delay = max(0.1, self.delay - 0.001)  # Prevent negative delay

    def update_score_display(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

    def check_self_collision(self):
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                self.reset_game()

    def reset_game(self):
        time.sleep(1)
        self.head.goto(0, 0)
        self.head.direction = "stop"
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.score = 0
        self.delay = 0.1
        self.update_score_display()

    def move_segments(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(self.segments[index - 1].pos())
        if self.segments:
            self.segments[0].goto(self.head.pos())

if __name__ == "__main__":
    SimpleSnakeGame()

