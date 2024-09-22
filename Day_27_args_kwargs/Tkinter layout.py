from tkinter import *


def button_clicked():
    my_label.config(text=input.get())


# Screen
window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10) # padding aur same technique se kisi me bhi padding de skte he.

# Label
my_label = Label(text="It is a label",font=("Arial",24,"bold"))
my_label.config(text="New Text")
# ____________________
# my_label.pack() # Pack each of the widget with each other(Matlab ki har ek widget ko ek doosre se jod ke rkhta he
# jo widget pehle pack hoga agla uske baad niche hi ayega is pack ki vja se lekin aap isko change kar skte se side bta
# ke lekin ek place() nam se attribute he jisme proper x aur y cordinate bta ke widget ki jga bta skte he)
# _________________________
# my_label.place(x=150,y=150) # x and y cordinates ki range apki window size pe depend karenge
# _________________________________
my_label.grid(column=0, row=0) # Sbse best yahi he (But ek hi program me pack() place() grid() sath me nhi aa skte koi ek use karo)

# Button
button = Button(text="Click me!", command=button_clicked)
# button.pack() # Pack each of the widget with each other
button.grid(column=0, row=1)





# Entry
input = Entry(width=20)
print(input.get())
# input.pack() # Pack each of the widget with each other
input.grid(column=0,row=2)

window.mainloop()