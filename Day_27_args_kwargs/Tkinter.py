# GUI

import tkinter

window = tkinter.Tk()
window.title("My first GUI Program") # Title bnane ke lie
window.minsize(width=500, height=300)

# Label kese bnaye
my_label = tkinter.Label(text="It is a label",font=("Arial",24,"bold")) # lekin khali isse kuch bhi nhi bna hua dikhega
# my_label.pack() # isse label dikhne lgega
# my_label.pack(side="bottom") # Yha side me aap top , bottom, left , right bhar ke lable ki position decide kar skte he
# tkinter documetation dekhe iske lie
#                                                tkinter documentation
#                                                https://docs.python.org/3/library/tkinter.html#the-packer
# my_label.pack(expand=True) # Isse poori screen ki jga gher ke beech me ajyega
my_label.pack()




# Ye sbse last me lgna chiye
window.mainloop() # humne jo window(Screen) bnayi he use chalu rkhne ke lie taki vo aate hi gayab na hojaye

