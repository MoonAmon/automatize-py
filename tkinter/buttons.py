from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! You click me!!")
    myLabel.pack()


myButton = Button(root, text="Click me!", command=myClick, fg="blue")
myButton.pack()


root.mainloop()