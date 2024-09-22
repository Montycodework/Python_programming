from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red","green","blue","yellow","orange"]


tim = Turtle(shape="turtle")
tim.color("blue")
tim.penup()
tim.goto(x=-230, y=-100)


screen.exitonclick()
