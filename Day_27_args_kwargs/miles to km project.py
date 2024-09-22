from tkinter import *

# Function to convert the miles to km
def mile_to_km():
    miles = float(miles_input.get())
    km = int(miles * 1.609)
    output_label.config(text=km)


#Screen
window = Tk()
window.title("Miles to KM Converter")
# window.minsize(width=300,height=150)
window.config(padx=20, pady=20)


# Input

miles_input = Entry(width=10)
miles_input.grid(column=1,row=0)


# labels
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

output_label = Label(text="0")
output_label.grid(column=1,row=1)

km_label = Label(text="KM")
km_label.grid(column=2,row=1)

# Button
claculate_button = Button(text="Calculate", command=mile_to_km)
claculate_button.grid(column=1,row=2)
# claculate_button.config(padx=5,pady=5)

window.mainloop()