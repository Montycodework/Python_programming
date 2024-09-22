from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward(): # This function is used as input to move the turtle for move forwrd by space key
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun= move_forward) # Here move_forward function is used without () as an input 
screen.exitonclick()