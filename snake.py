from turtle import Turtle
from food import Food

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def   __init__(self):
        self.all_segments = []
        self.create_snake()
        self.head = self.all_segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.all_segments.append(new_segment)

    def move(self):
        for snake_num in range(len(self.all_segments) - 1, 0, -1):
            x_cor = self.all_segments[snake_num - 1].xcor()
            y_cor = self.all_segments[snake_num - 1].ycor()
            self.all_segments[snake_num].goto(x=x_cor, y=y_cor)
        self.head.fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.all_segments:
            seg.goto(x= 2000, y= 2000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]