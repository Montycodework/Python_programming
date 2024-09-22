import turtle as t
import random

tim = t.Turtle()
t.colormode(255) # for tha random  R G B colors

def random_colors(): # This function is made up for random RGB vaues for random coloring
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)
    random_color = (r,g,b)
    return random_color

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", 
# "SeaGreen"]
direction = [0,90, 180, 270]
tim.pensize(10)
tim.speed("fastest")
for i in range(100):
    # tim.color(random.choice(colours)) # In this line we are using limited numbers of colors by list
    tim.color(random_colors()) # For Random colors with t.colormode(255)
    tim.forward(20)
    tim.setheading(random.choice(direction))


