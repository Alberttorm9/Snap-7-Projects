import tkinter as tk

# Función para mover el círculo a las coordenadas del clic derecho
def move_circle(event):
    canvas.coords(circle, event.x-10, event.y-10, event.x+10, event.y+10)

# Crear la ventana y el lienzo
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Crear el círculo en el lienzo
circle = canvas.create_oval(190, 190, 210, 210, fill="blue")

# Vincular el evento de clic derecho a la función de mover el círculo
canvas.bind("<Button-3>", move_circle)

# Iniciar la aplicación
root.mainloop()