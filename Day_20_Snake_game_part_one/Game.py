from turtle import Screen
# Yha se Turtle class ko hta dia kyuki
# hum usko ab use nhi kar rhe he hum apni bnayi hui
# class use kar rhe he turtle ke function use k
from Snakeclass import Snake
from food import Food
from scoreboard import Scoreboard
import time


# snake = Turtle("square") # yha aap brackets me hi shape bhi mention kar skte ho
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
# starting_position = [(0,0),(-20,0),(-40,0)]
# segments = []

# Creating the snake
# for i in starting_position:
#     snake = Turtle("square")
#     snake.color("white")
#     # snake.shape("square") # Hum isko uper direct line no 4 me bhi set kar skte he
#     snake.penup()
#     snake.goto(i)
#     segments.append(snake)

#Controlling the snake

#1. Keys binding by screen.listen
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



# Moving the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # for seg in segments: (this loop only help u to move forward it do not help you to turn
    #     seg.forward(20)
        # screen.update()
    # for seg_num in range(start=1, stop=3, step=1) this range function is comes from c language and gives u error.
    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_y,new_x)
    # segments[0].forward(20)
    # segments[0],left(90)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     score.game_over()
    #
    #
    #
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         score.game_over()

screen.exitonclick()



# You can learn list slicing after complete this game.