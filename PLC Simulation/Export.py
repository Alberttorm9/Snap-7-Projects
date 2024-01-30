import tkinter as tk
from PIL import Image, ImageTk
import os
import snap7

plc = snap7.logo.Logo()
plc.connect('192.168.30.102', 0, 1)

def on_Peticion_Salida():
    plc.write("V60.5", 1)
    canvas.itemconfig(boton_Peticion_Salida, image=Boton2_Image)

def off_Peticion_Salida():
    plc.write("V60.5", 0)
    canvas.itemconfig(boton_Peticion_Salida, image=Boton_Image)

def on_Solicitud_Checkin():
    plc.write("V60.3", 1)
    canvas.itemconfig(boton_Solicitud_Checkin, image=Boton2_Image)

def off_Solicitud_Checkin():
    plc.write("V60.3", 0)
    canvas.itemconfig(boton_Solicitud_Checkin, image=Boton_Image)

def on_Pulsador_Garaje():
    plc.write("V60.6", 1)
    canvas.itemconfig(boton_Garaje, image=Boton2_Image)

def off_Pulsador_Garaje():
    plc.write("V60.6", 0)
    canvas.itemconfig(boton_Garaje, image=Boton_Image)

def on_Pulsador_Perimetro():
    plc.write("V60.4", 1)
    canvas.itemconfig(boton_Perimetro, image=Boton2_Image)

def off_Pulsador_Perimetro():
    plc.write("V60.4", 0)
    canvas.itemconfig(boton_Perimetro, image=Boton_Image)

def on_Pulsador_Limpieza():
    plc.write("V60.2", 1)
    canvas.itemconfig(boton_Limpieza, image=Boton2_Image)

def off_Pulsador_Limpieza():
    plc.write("V60.2", 0)
    canvas.itemconfig(boton_Limpieza, image=Boton_Image)

def on_sensor_cerrado():
    if plc.read("V90.0"):
        plc.write("V80.0", 0)
        canvas.itemconfig(sensor_cerrado, image=Sensor2_Image)
    else:
        plc.write("V80.0", 1)
        canvas.itemconfig(sensor_cerrado, image=Sensor_Image)

def on_sensor_abierto():
    if plc.read("V90.1"):
        plc.write("V80.1", 0)
        canvas.itemconfig(sensor_abierto, image=Sensor2_Image)
    else:
        plc.write("V80.1", 1)
        canvas.itemconfig(sensor_abierto, image=Sensor_Image)

def on_sensor_puerta():
    if plc.read("V90.2"):
        plc.write("V80.2", 0)
        canvas.itemconfig(sensor_puerta, image=Sensor4_Image)
    else:
        plc.write("V80.2", 1)
        canvas.itemconfig(sensor_puerta, image=Sensor3_Image)

def on_right_click(event):
    x = event.x
    y = event.y
    print(f"Posición del clic derecho - X: {x}, Y: {y}")


def actualizar():
    if plc.read("V90.0"):
        canvas.itemconfig(Portal, image=Portal2_Image)
    elif plc.read("V90.1"):
        canvas.itemconfig(Portal, image=Portal_Image)
    else:
        canvas.itemconfig(Portal, image=Portal3_Image)

    if plc.read("V90.2"):
        canvas.itemconfig(Puerta, image=Puerta2_Image)
    else:
        canvas.itemconfig(Puerta, image=Puerta_Image)
    root.after(100, actualizar)

root = tk.Tk()
root.title("Exportar Información")
root.config(bg='#505050')

Plano_image = ImageTk.PhotoImage(file=os.path.abspath("PLANO.png"))
Boton_Image = ImageTk.PhotoImage(file=os.path.abspath("Boton.png"))
Boton2_Image = ImageTk.PhotoImage(file=os.path.abspath("Boton2.png"))


porcentaje = 70
Sensor_Image = Image.open(os.path.abspath("Sensor.png"))
Sensor_Image.thumbnail((int(Sensor_Image.width * (porcentaje / 100)), int(Sensor_Image.height * (porcentaje / 100))))
Sensor_Image = ImageTk.PhotoImage(Sensor_Image)
Sensor2_Image = Image.open(os.path.abspath("Sensor2.png"))
Sensor2_Image.thumbnail((int(Sensor2_Image.width * (porcentaje / 100)), int(Sensor2_Image.height * (porcentaje / 100))))
Sensor2_Image = ImageTk.PhotoImage(Sensor2_Image)

porcentaje = 25
Sensor3_Image = Image.open(os.path.abspath("Sensor.png"))
Sensor3_Image.thumbnail((int(Sensor3_Image.width * (porcentaje / 100)), int(Sensor3_Image.height * (porcentaje / 100))))
Sensor3_Image = ImageTk.PhotoImage(Sensor3_Image)
Sensor4_Image = Image.open(os.path.abspath("Sensor2.png"))
Sensor4_Image.thumbnail((int(Sensor4_Image.width * (porcentaje / 100)), int(Sensor4_Image.height * (porcentaje / 100))))
Sensor4_Image = ImageTk.PhotoImage(Sensor4_Image)

Puerta_Image = ImageTk.PhotoImage(file=os.path.abspath("Puerta_Abierta.png"))
Puerta2_Image = ImageTk.PhotoImage(file=os.path.abspath("Puerta_Cerrada.png"))

Portal_Image = Image.open(os.path.abspath("Portal_Abierto.png"))
Portal_Image = Portal_Image.resize((150, 150))
Portal_Image = ImageTk.PhotoImage(Portal_Image)
Portal2_Image = Image.open(os.path.abspath("Portal_Cerrado.png"))
Portal2_Image = Portal2_Image.resize((150, 150))
Portal2_Image = ImageTk.PhotoImage(Portal2_Image)
Portal3_Image = Image.open(os.path.abspath("Portal_Mitad.png"))
Portal3_Image = Portal3_Image.resize((150, 150))
Portal3_Image = ImageTk.PhotoImage(Portal3_Image)



canvas = tk.Canvas(root, width=Plano_image.width(), height=Plano_image.height(), bd=0, highlightthickness=0)
canvas.pack()

canvas.create_image(0, 0, image=Plano_image, anchor='nw')
canvas.bind('<Button-3>', on_right_click)



boton_Peticion_Salida = canvas.create_image(203, 26, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Peticion_Salida, '<Button-1>', lambda e: on_Peticion_Salida())
canvas.tag_bind(boton_Peticion_Salida, '<ButtonRelease-1>', lambda e: on_Peticion_Salida())

boton_Solicitud_Checkin = canvas.create_image(920, 180, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Solicitud_Checkin, '<Button-1>', lambda e: on_Solicitud_Checkin())
canvas.tag_bind(boton_Solicitud_Checkin, '<ButtonRelease-1>', lambda e: off_Solicitud_Checkin())

boton_Garaje = canvas.create_image(1160, 510, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Garaje, '<Button-1>', lambda e: on_Pulsador_Garaje())
canvas.tag_bind(boton_Garaje, '<ButtonRelease-1>', lambda e: off_Pulsador_Garaje())


boton_Perimetro = canvas.create_image(690, 492, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Perimetro, '<Button-1>', lambda e: on_Pulsador_Perimetro())
canvas.tag_bind(boton_Perimetro, '<ButtonRelease-1>', lambda e: off_Pulsador_Perimetro())

boton_Limpieza = canvas.create_image(720, 492, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Limpieza, '<Button-1>', lambda e: on_Pulsador_Limpieza())
canvas.tag_bind(boton_Limpieza, '<ButtonRelease-1>', lambda e: off_Pulsador_Limpieza())

if plc.read("V90.0"):
    sensor_cerrado = canvas.create_image(1800, 430, image=Sensor_Image, anchor=tk.CENTER)
else:
    sensor_cerrado = canvas.create_image(1800, 430, image=Sensor2_Image, anchor=tk.CENTER)
canvas.tag_bind(sensor_cerrado, '<Button-1>', lambda e: on_sensor_cerrado())

if plc.read("V90.1"):
    sensor_abierto = canvas.create_image(1800, 120, image=Sensor_Image, anchor=tk.CENTER)
else:
    sensor_abierto = canvas.create_image(1800, 120, image=Sensor2_Image, anchor=tk.CENTER)
canvas.tag_bind(sensor_abierto, '<Button-1>', lambda e: on_sensor_abierto())

if plc.read("V90.2"):
    sensor_puerta = canvas.create_image(895, 180, image=Sensor3_Image, anchor=tk.CENTER)
else:
    sensor_puerta = canvas.create_image(895, 180, image=Sensor4_Image, anchor=tk.CENTER)
canvas.tag_bind(sensor_puerta, '<Button-1>', lambda e: on_sensor_puerta())

Puerta = canvas.create_image(890, 100, anchor=tk.CENTER)
Portal = canvas.create_image(1780, 280, anchor=tk.CENTER)

actualizar()

root.mainloop()