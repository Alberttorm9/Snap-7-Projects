import tkinter as tk

def mostrar_numero(event, numero):
    print("El cuadrado pulsado tiene el número:", numero)

root = tk.Tk()
root.geometry("550x100")

canvas = tk.Canvas(root, width=500, height=50)
canvas.pack()

# Dibujar los cuadrados y asociar un número a cada uno
for i in range(10):
    x0 = i * 50
    x1 = x0 + 50
    canvas.create_rectangle(x0, 0, x1, 50, fill="lightblue")
    canvas.tag_bind("cuadrado"+str(i+1), "<Button-1>", lambda event, num=i+1: mostrar_numero(event, num))
    canvas.create_text(x0+25, 25, text=str(i+1), font=("Arial", 12), tags="cuadrado"+str(i+1))

root.mainloop()