import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Cuadrícula en el centro de la pantalla")

# Definir el tamaño de la pantalla
screen_width = 1920
screen_height = 1080

# Definir el tamaño de la cuadrícula
grid_width = 5
grid_height = 5

# Crear un frame para contener la cuadrícula
frame = tk.Frame(root)
frame.pack(expand=True)

# Calcular las coordenadas para el centro de la pantalla
x_center = screen_width // 2
y_center = screen_height // 2

# Crear y posicionar los widgets en la cuadrícula
for i in range(grid_height):
    for j in range(grid_width):
        label = tk.Label(frame, text=f"({i},{j})", borderwidth=1, relief="solid", width=10, height=2)
        label.grid(row=i, column=j)

# Posicionar la cuadrícula en el centro de la ventana
frame.grid(row=0, column=0, padx=(x_center - (grid_width*100)//2), pady=(y_center - (grid_height*50)//2))

# Ejecutar la aplicación
root.mainloop()