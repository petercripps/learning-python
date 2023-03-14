from tkinter import *  
root = Tk()  

for fm in ['blue','red','yellow','green','white','black']:  
    Frame(height = 60,width = 640,bg = fm).pack()  
root.mainloop() 