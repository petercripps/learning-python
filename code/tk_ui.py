# Example UI using tkinter
# See: https://www.tutorialspoint.com/python/python_gui_programming.htm
from tkinter import *

window = Tk()

window.geometry("500x200")

def say_hello():
    print("Hello")

b1 = Button(window, text="Okay", command=say_hello)
b2 = Button(window, text="Cancel")

b1.pack(padx=5, pady=5, side=LEFT)
b2.pack(padx=5, pady=5, side=LEFT)
# b1.grid(row=6,column=4)
# b2.grid(row=6,column=5)

window.mainloop()