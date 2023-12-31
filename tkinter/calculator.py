import re
from tkinter import *
import math

root = Tk()
root.title("Simple Calculator")

font = ('Arial', 12)

e = Entry(root, width=35, borderwidth=5, font=font)
e.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

text_box = Text(root, width=35, height=5, borderwidth=4)
text_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def getSegundoNum(input):
    pattern = r'\W+(\d+)'
    match = re.search(pattern, input)
    return match.group(1)
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)
    text_box.delete(1.0, END)



def button_equal():
    second_number = getSegundoNum(e.get())
    e.delete(0, END)

    if math == "addiction":
        result = f_num + int(second_number)
        e.insert(0, result)
        text_box.insert(END, f"{f_num} + {second_number} = {result}\n")
    elif math == "divide":
        result = f_num / int(second_number)
        e.insert(0, result)
        text_box.insert(END, f"{f_num} / {second_number} = {result}\n")
    elif math == "multiply":
        result = f_num * int(second_number)
        e.insert(0, result)
        text_box.insert(END, f"{f_num} * {second_number} = {result}\n")
    elif math == "subtract":
        result = f_num - int(second_number)
        e.insert(0, result)
        text_box.insert(END, f"{f_num} - {second_number} = {result}\n")

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addiction"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(END, f"{f_num}+")

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.insert(0, str("*"))
    e.delete(0, END)
    e.insert(END, f"{f_num}*")


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(END, f"{f_num}-")

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(END, f"{f_num}/")

def button_square():
    first_number = e.get()
    global f_num
    f_num = math.sqrt(int(first_number))
    e.delete(0, END)
    text_box.insert(END, f"√{first_number} = {f_num}\n")
    e.insert(0, f_num)

def button_del():
    current = e.get()
    e.delete(len(current)-1, END)


# Define buttons

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=80, pady=20, command=button_clear)

button_subtract = Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=button_divide)

button_square = Button(root, text="√", padx=40, pady=20, command=button_square)
button_del = Button(root, text="←", padx=80, pady=20, command=button_del)

# Put buttons on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)

button_divide.grid(row=7, column=0)
button_multiply.grid(row=7, column=1)
button_subtract.grid(row=7, column=2)

button_square.grid(row=8, column=0)
button_del.grid(row=8, column=1, columnspan=2)


root.mainloop()