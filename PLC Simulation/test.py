import tkinter as tk
from PIL import Image, ImageTk
import os

def on_button_press():
    print("El botón ha sido presionado")

def on_button_press2():
    print("El botón ha sido presionado 2")

root = tk.Tk()
root.title("Exportar Información")
root.config(bg='#505050')

Plano = ImageTk.PhotoImage(file=os.path.abspath("PLANO.png"))
Boton = ImageTk.PhotoImage(file=os.path.abspath("Boton.png"))

canvas = tk.Canvas(root, width=Plano.width(), height=Plano.height(), bd=0, highlightthickness=0)
canvas.pack()

canvas.create_image(0, 0, image=Plano, anchor='nw')
boton_Peticion_Salida = canvas.create_image(203, 26, image=Boton, anchor='nw')
boton_Solicitud_Checkin = canvas.create_image(950, 160, image=Boton, anchor='nw')

canvas.tag_bind(boton_Peticion_Salida, '<Button-1>', lambda e: on_button_press())
canvas.tag_bind(boton_Solicitud_Checkin, '<Button-1>', lambda e: on_button_press2())

root.mainloop()
