import turtle as tk
import random
# num_sides = 6
# angle = 360 / num_sides
colours = ["blue", "green", "red","orange"]
tk.pensize(5)
def shapes(num_sides):
    angle = 360 / num_sides
    for i in range (num_sides):
        tk.forward(100)
        tk.right(angle)
       
for _ in range(3,9):
    # num_sides = _
    # shapes(num_sides)
    tk.color(random.choice(colours))
    shapes(_) # This is short mwethod 

