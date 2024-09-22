from turtle import Turtle
#________________________________________________________________________
# Constant are all capital in class
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Constant are all capital in class
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
#_______________________________________________________________________
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # Instead of using self.segments[0] use self.head only

    def create_snake(self):
        for position in STARTING_POSITIONS:
            # snake = Turtle("square")
            # snake.color("white")
            # # snake.shape("square") # Hum isko uper direct line no 4 me bhi set kar skte he
            # snake.penup()
            # snake.goto(i)
            # self.segments.append(snake)
            self.add_segment(position)

    def add_segment(self,position):
        snake = Turtle("square")
        snake.color("white")
        # snake.shape("square") # Hum isko uper direct line no 4 me bhi set kar skte he
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # self.segments[0].forward(MOVE_DISTANCE)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
        # self.segments[0].setheading(90) start
        # self.head.setheading(90)  updated version of above
            self.head.setheading(UP) # Most advance version of above

    def down(self):
        if self.head.heading() != UP:
        # self.segments[0].setheading(270) start
        # self.head.setheading(270)  updated version of above
            self.head.setheading(DOWN) # Most advance version of above

    def left(self):
        if self.head.heading() != RIGHT:
        # self.segments[0].setheading(180) start
        # self.head.setheading(180) updated version of above
            self.head.setheading(LEFT) # Most advance version of above

    def right(self):
        if self.head.heading() != LEFT:
        # self.segments[0].setheading(0) start
        # self.head.setheading(0)  updated version of above
            self.head.setheading(RIGHT) # Most advance version of above




