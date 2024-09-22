# import tkinter
from tkinter import *

# For making screen
# ____________________________________
# window = tkinter.Tk()
window = Tk()
window.title("My first GUI Program") # Title bnane ke lie
window.minsize(width=500, height=300)


# ______________________________
# Labels
# my_label = tkinter.Label(text="It is a label",font=("Arial",24,"bold"))
my_label = Label(text="It is a label",font=("Arial",24,"bold"))

# my_label.pack(side = "left")
my_label.pack() # for making it into the center top

my_label["text"] = "New text"
my_label.config(text = "New text")

# __________________________________
#Buttons

# button = tkinter.button() # Isko asaan bnane ke lie window  = Tk() kardo
# button = Button(text="Click me!")
# button.pack()

# def button_clicked():
#     print("I got clicked")
#
# button = Button(text="Click me!", command=button_clicked) # Command ki vja se function trigger hoke print kardega
# button.pack()

# _____________________________________________________
# # Challange to change the label by button click
# def button_clicked():
#     # my_label["text"] = "Text changed"
#     #              or
#     my_label.config(text = "Text changed")
# button = Button(text="Click me!", command=button_clicked)
# button.pack()

# Successfull
# ____________________________________________________________
# Input command


# input = Entry()
# input.pack()

input = Entry(width=10) # Input ki width set krne ke lie
input.pack()

# input.get() # To get the text from input box
# __________________________________________________


# challange to get the text inside input on label when button clicked
def button_clicked():
    my_label.config(text = input.get())
button = Button(text="Click me!", command=button_clicked)
button.pack()

# successfull

window.mainloop()