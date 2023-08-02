import random
import tkinter as tk

root = tk.Tk()
root.title("Exibir array.")

canvas = tk.Canvas(root, bg="white", height=200, width=400)
canvas.pack()

data = [10]

def create_new_string(length):
    new_list = [random.randint(1, 300) for _ in range(length)]
    return new_list
def update_data():
    global data
    data = create_new_string(10)
    draw_bar_chart(data)
def draw_bar_chart(data):
    canvas.delete("all")

    max_value = max(data)
    bar_width = 30
    chart_height = 150
    chart_width = (bar_width + 10) * len(data)
    x = 50

    for value in data:
        bar_height = (value / max_value) * chart_height
        canvas.create_rectangle(x, chart_height - bar_height, x + bar_width, chart_height, fill="black")
        canvas.create_text(x + bar_width // 2, chart_height + 5, text=str(value))
        x += bar_width + 10

draw_bar_chart(data)
button_new = tk.Button(root, text="Create new string", command=update_data)
button_new.pack()

root.mainloop()