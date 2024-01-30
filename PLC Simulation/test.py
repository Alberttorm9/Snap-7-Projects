import tkinter as tk
from PIL import Image, ImageTk
import os
import snap7

plc = snap7.logo.Logo()

def on_button_press():
    print("El botón ha sido presionado")

def on_button_release():
    print("El botón ha sido Soltado")

def on_button_release2():
    print("El botón ha sido Soltado 2")

def on_button_press2():
    print("El botón ha sido presionado 2")

def on_button_press3():
    print("El botón ha sido presionado 3")

def on_button_release3():
    print("El botón ha sido Soltado 3")

def on_button_press4():
    print("El botón ha sido presionado 4")

def on_button_release4():
    print("El botón ha sido Soltado 4")

def on_button_press5():
    print("El botón ha sido presionado 5")

def on_button_release5():
    print("El botón ha sido Soltado 5")

def on_right_click(event):
    x = event.x
    y = event.y
    print(f"Posición del clic derecho - X: {x}, Y: {y}")


def actualizar():
    if True:  # Reemplaza "variable_activa" con el nombre de tu variable
        canvas.itemconfig(Puerta, image=Puerta2_Image)
    root.after(1000, actualizar)

root = tk.Tk()
root.title("Exportar Información")
root.config(bg='#505050')

Plano_image = ImageTk.PhotoImage(file=os.path.abspath("PLANO.png"))
Boton_Image = ImageTk.PhotoImage(file=os.path.abspath("Boton.png"))
Puerta_Image = ImageTk.PhotoImage(file=os.path.abspath("Puerta_Abierta.png"))
Puerta2_Image = ImageTk.PhotoImage(file=os.path.abspath("Puerta_Cerrada.png"))
Portal_Image = ImageTk.PhotoImage(file=os.path.abspath("Portal_Abierto.png"))
Portal2_Image = ImageTk.PhotoImage(file=os.path.abspath("Portal_Cerrado.png"))
Portal3_Image = ImageTk.PhotoImage(file=os.path.abspath("Portal_Mitad.png"))

canvas = tk.Canvas(root, width=Plano_image.width(), height=Plano_image.height(), bd=0, highlightthickness=0)
canvas.pack()

canvas.create_image(0, 0, image=Plano_image, anchor='nw')
canvas.bind('<Button-3>', on_right_click)



boton_Peticion_Salida = canvas.create_image(203, 26, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Peticion_Salida, '<Button-1>', lambda e: on_button_press())
canvas.tag_bind(boton_Peticion_Salida, '<ButtonRelease-1>', lambda e: on_button_release())

boton_Solicitud_Checkin = canvas.create_image(920, 180, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Solicitud_Checkin, '<Button-1>', lambda e: on_button_press2())
canvas.tag_bind(boton_Solicitud_Checkin, '<ButtonRelease-1>', lambda e: on_button_release2())

boton_Garaje = canvas.create_image(1160, 510, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Garaje, '<Button-1>', lambda e: on_button_press3())
canvas.tag_bind(boton_Garaje, '<ButtonRelease-1>', lambda e: on_button_release3())


boton_Perimetro = canvas.create_image(690, 492, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Perimetro, '<Button-1>', lambda e: on_button_press4())
canvas.tag_bind(boton_Perimetro, '<ButtonRelease-1>', lambda e: on_button_release4())

boton_Limpieza = canvas.create_image(720, 492, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Limpieza, '<Button-1>', lambda e: on_button_press5())
canvas.tag_bind(boton_Limpieza, '<ButtonRelease-1>', lambda e: on_button_release5())

Puerta = canvas.create_image(720, 492, image=Puerta_Image, anchor='nw')

actualizar()

root.mainloop()