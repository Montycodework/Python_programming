from turtle import Turtle, Screen, back

tim = Turtle()
screen = Screen()

def forwards():
    tim.forward(10)
def backwards():
    tim.back(10)    
def up():
    tim.left(10)
def down():
    tim.right(10)
def clears():
    tim.clear()
    tim.penup()  
    tim.home() # to make the turtle on (0,0) cordinates  
    tim.pendown()

screen.listen()
# screen.onkey(key="d",fun=forwards)    
screen.onkey(forwards, "d")    
# screen.onkey(key="a",fun=backwards)
screen.onkey(backwards, "a")    
# screen.onkey(key="w",fun=up)
screen.onkey(up, "w")    
# screen.onkey(key="s",fun=down)
screen.onkey(down, "s")    
screen.onkey(clears, "space")    
screen.exitonclick()    