import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200, bg='black')
canvas.pack()

# Crear un rectángulo en el lienzo
canvas.create_rectangle(50, 50, 150, 150, fill='lightblue')

# Colocar texto en el lienzo
text = canvas.create_text(100, 100, text="Ejemplo de texto", fill="black")

root.mainloop()