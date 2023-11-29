import tkinter as tk

# Función para leer el valor del archivo y configurar el color del cuadrado
def actualizar_cuadrado():
    # Lee el contenido del archivo
    with open('Snap-7-Projects\Prueba\color.txt', 'r') as file:
        contenido = file.read()
    
    # Comprueba el valor leído y configura el color del cuadrado
    if contenido.strip() == '1':
        canvas.itemconfig(cuadrado, fill='blue')
    elif contenido.strip() == '2':
        canvas.itemconfig(cuadrado, fill='red')
    
    # Vuelve a llamar a la función después de un intervalo de tiempo (en milisegundos)
    ventana.after(1000, actualizar_cuadrado)  # Cambia el valor 1000 según tus necesidades

# Crea la ventana de tkinter
ventana = tk.Tk()
ventana.title('Programa B')

# Crea un lienzo (canvas) y dibuja un cuadrado
canvas = tk.Canvas(ventana, width=200, height=200)
cuadrado = canvas.create_rectangle(50, 50, 150, 150, fill='blue')
canvas.pack()

# Inicia la actualización del cuadrado
actualizar_cuadrado()

# Ejecuta el bucle principal de la ventana
ventana.mainloop()