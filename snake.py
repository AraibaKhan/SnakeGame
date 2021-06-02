from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SPEED = ["slow", "normal", "fast", "fastest"]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_block(position)

    def add_block(self, position):
        new_block = Turtle(shape="square")
        new_block.color("white")
        new_block.turtlesize()
        new_block.penup()
        new_block.goto(position)
        self.segment.append(new_block)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        self.add_block(self.segment[-1].position())

    def move(self):
        # range(start point, end point, step size)
        for element in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[element - 1].xcor()
            new_y = self.segment[element - 1].ycor()
            self.segment[element].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.head.speed("fastest")

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.head.speed("fastest")

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.head.speed("fastest")

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.head.speed("fastest")
