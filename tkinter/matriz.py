import tkinter as tk

root = tk.Tk()
root.title("Matriz")
turn = "X"
font = ('Arial', 50)
def on_clicadoX(event):
    global turn
    turn = "O"
    # Obtém o rótulo clicado
    rotulo_clicado = event.widget

    # Obtem a posição do rótulo na matriz
    x = rotulo_clicado.grid_info()["row"]
    y = rotulo_clicado.grid_info()["column"]

    # Muda o valor correspondente na matriz
    matriz_exemplo[x][y] = "X"

    # Atualiza o texto do rotulo com o valor correspondente na matriz
    rotulo_clicado.config(text=matriz_exemplo[x][y], font=font)

def on_clicado0(event):
    global turn
    turn = "X"
    # Obtém o rótulo clicado
    rotulo_clicado = event.widget

    # Obtem a posição do rótulo na matriz
    x = rotulo_clicado.grid_info()["row"]
    y = rotulo_clicado.grid_info()["column"]

    # Muda o valor correspondente na matriz
    matriz_exemplo[x][y] = "O"

    # Atualiza o texto do rotulo com o valor correspondente na matriz
    rotulo_clicado.config(text=matriz_exemplo[x][y], font=font)

def jogada(event):
    if turn == "X":
        return on_clicadoX(event)
    else:
        return on_clicado0(event)


def exibir_matriz():
    for y in range(3):
        for x in range(3):
            label = tk.Label(root, text=matriz_exemplo[x][y], font=font)
            label.grid(row=x, column=y, padx=10, pady=10)
            label.bind("<Button-1>", jogada)

def reset_button(matriz_exemplo):
    for y in range(3):
        for x in range(3):
            matriz_exemplo[x][y] = "   "
    return exibir_matriz()

matriz_exemplo = [
    ["  ", "  ", "  "],
    ["  ", "  ", "  "],
    ["  ", "  ", "  "]
]

button_reset = tk.Button(root, padx=30, pady=30, text="Reset",command=lambda:reset_button(matriz_exemplo))
button_reset.grid(row=3, column=1)

exibir_matriz()

root.mainloop()