import tkinter as tk
from PIL import Image, ImageTk
import os
import snap7

plc = snap7.logo.Logo()
plc.connect('192.168.30.102', 0, 1)
plc.write("V60.7", 1)
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
    if plc.read("V61.0"):
        plc.write("V61.0", 0)
        canvas.itemconfig(boton_Limpieza, image=Boton_Image)
    else:
        plc.write("V61.0", 1)
        canvas.itemconfig(boton_Limpieza, image=Boton2_Image)
def on_Checkin_ok():
    plc.write("V60.1", 1)
    canvas.itemconfig(boton_CheckinOK, image=Boton2_Image)

def off_Checkin_ok():
    plc.write("V60.1", 0)
    canvas.itemconfig(boton_CheckinOK, image=Boton3_Image)

def on_Checkout_ok():
    plc.write("V60.2", 1)
    canvas.itemconfig(boton_CheckoutOK, image=Boton2_Image)

def off_Checkout_ok():
    plc.write("V60.2", 0)
    canvas.itemconfig(boton_CheckoutOK, image=Boton_Image)

def on_Limpieza():
    if plc.read("V60.0"):
        plc.write("V60.0", 0)
        canvas.itemconfig(selector_Limpieza, image=SelectorOff)
    else:
        plc.write("V60.0", 1)
        canvas.itemconfig(selector_Limpieza, image=SelectorOn)

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
    canvas.coords(Trabajador, x, y)

def on_mid_click(event):
    x = event.x
    y = event.y
    canvas.coords(Usuario, x, y)

def actualizar():

    if plc.read("V50.4"):
        canvas.itemconfig(luz_estados, image=Boton_Image)
    elif plc.read("V50.3"):
        canvas.itemconfig(luz_estados, image=Boton3_Image)
    elif plc.read("V50.2"):
        canvas.itemconfig(luz_estados, image=Boton2_Image)
    else:
        canvas.itemconfig(luz_estados, image=BotonX_Image)

    if plc.read("V51.1"):
        canvas.itemconfig(Texto_Exterior, text="En Limpieza") 
    elif plc.read("V51.2"):
        canvas.itemconfig(Texto_Exterior, text="Habitación Libre") 
    elif plc.read("V51.3"):
        canvas.itemconfig(Texto_Exterior, text="Esperando Salida")
    else: 
        canvas.itemconfig(Texto_Exterior, text="")
        
    if plc.read("V50.1"):
        canvas.itemconfig(Puerta, image=Puerta_Image)
    else:
        canvas.itemconfig(Puerta, image=Puerta2_Image)
        
    if plc.read("V50.0"):
        canvas.itemconfig(portal_Abriendose, image=BotonZ_Image)
    else:
        canvas.itemconfig(portal_Abriendose, image="")

    if plc.read("V50.5"):
        canvas.itemconfig(luz_perimetro, image=Red_Light_Image)
    elif plc.read("V50.6"):
        canvas.itemconfig(luz_perimetro, image=Green_Light_Image)
    elif plc.read("V50.7"):
        canvas.itemconfig(luz_perimetro, image=Blue_Light_Image)
    else:
        canvas.itemconfig(luz_perimetro, image=white_Light_off_Image)

    if plc.read("V51.0"):
        canvas.itemconfig(luz_blanca, image=white_Light_on_Image)
    else:
        canvas.itemconfig(luz_blanca, image=white_Light_off_Image)


    if plc.read("V90.0"):
        canvas.itemconfig(Portal, image=Portal2_Image)
    elif plc.read("V90.1"):
        canvas.itemconfig(Portal, image=Portal_Image)
    else:
        canvas.itemconfig(Portal, image=Portal3_Image)

    root.after(100, actualizar)


root = tk.Tk()
root.title("Exportar Información")
root.config(bg='#505050')

porcentaje = 50
Trabajador_Image = Image.open(os.path.abspath("Trabajador.png"))
Trabajador_Image.thumbnail((int(Trabajador_Image.width * (porcentaje / 100)), int(Trabajador_Image.height * (porcentaje / 100))))
Trabajador_Image = ImageTk.PhotoImage(Trabajador_Image)
Usuario_Image = Image.open(os.path.abspath("Usuario.png"))
Usuario_Image.thumbnail((int(Usuario_Image.width * (porcentaje / 100)), int(Usuario_Image.height * (porcentaje / 100))))
Usuario_Image = ImageTk.PhotoImage(Usuario_Image)

Plano_image = ImageTk.PhotoImage(file=os.path.abspath("PLANO.png"))
Boton_Image = ImageTk.PhotoImage(file=os.path.abspath("Boton.png"))
Boton2_Image = ImageTk.PhotoImage(file=os.path.abspath("Boton2.png"))
Boton3_Image = ImageTk.PhotoImage(file=os.path.abspath("Boton3.png"))
BotonX_Image = ImageTk.PhotoImage(file=os.path.abspath("BotonX.png"))
BotonZ_Image = ImageTk.PhotoImage(file=os.path.abspath("BotonZ.png"))
SelectorOff = ImageTk.PhotoImage(file=os.path.abspath("SelectorOff.png"))
SelectorOn = ImageTk.PhotoImage(file=os.path.abspath("SelectorOn.png"))

porcentaje = 50
Green_Light_Image = Image.open(os.path.abspath("Green_Light.png"))
Green_Light_Image.thumbnail((int(Green_Light_Image.width * (porcentaje / 100)), int(Green_Light_Image.height * (porcentaje / 100))))
Green_Light_Image = ImageTk.PhotoImage(Green_Light_Image)
Red_Light_Image = Image.open(os.path.abspath("Red_Light.png"))
Red_Light_Image.thumbnail((int(Red_Light_Image.width * (porcentaje / 100)), int(Red_Light_Image.height * (porcentaje / 100))))
Red_Light_Image = ImageTk.PhotoImage(Red_Light_Image)
Blue_Light_Image = Image.open(os.path.abspath("Blue_Light.png"))
Blue_Light_Image.thumbnail((int(Blue_Light_Image.width * (porcentaje / 100)), int(Blue_Light_Image.height * (porcentaje / 100))))
Blue_Light_Image = ImageTk.PhotoImage(Blue_Light_Image)
white_Light_on_Image = Image.open(os.path.abspath("Blanca_Encendida.png"))
white_Light_on_Image.thumbnail((int(white_Light_on_Image.width * (porcentaje / 100)), int(white_Light_on_Image.height * (porcentaje / 100))))
white_Light_on_Image = ImageTk.PhotoImage(white_Light_on_Image)
white_Light_off_Image = Image.open(os.path.abspath("Blanca_Apagada.png"))
white_Light_off_Image.thumbnail((int(white_Light_off_Image.width * (porcentaje / 100)), int(white_Light_off_Image.height * (porcentaje / 100))))
white_Light_off_Image = ImageTk.PhotoImage(white_Light_off_Image)


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

#####################################################################################################################################################


canvas = tk.Canvas(root, width=Plano_image.width(), height=Plano_image.height(), bd=0, highlightthickness=0)
canvas.pack()

canvas.create_image(0, 0, image=Plano_image, anchor='nw')
canvas.bind('<Button-2>', on_mid_click)
canvas.bind('<Button-3>', on_right_click)


#####################################################################################################################################################

#Peticion salida
boton_Peticion_Salida = canvas.create_image(203, 26, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Peticion_Salida, '<Button-1>', lambda e: on_Peticion_Salida())
canvas.tag_bind(boton_Peticion_Salida, '<ButtonRelease-1>', lambda e: off_Peticion_Salida())

#####################################################################################################################################################

#Solicitud CheckIn
boton_Solicitud_Checkin = canvas.create_image(920, 180, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Solicitud_Checkin, '<Button-1>', lambda e: on_Solicitud_Checkin())
canvas.tag_bind(boton_Solicitud_Checkin, '<ButtonRelease-1>', lambda e: off_Solicitud_Checkin())

#####################################################################################################################################################

#Boton Garaje
boton_Garaje = canvas.create_image(1160, 510, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Garaje, '<Button-1>', lambda e: on_Pulsador_Garaje())
canvas.tag_bind(boton_Garaje, '<ButtonRelease-1>', lambda e: off_Pulsador_Garaje())

#####################################################################################################################################################

#Boton Perimetro
boton_Perimetro = canvas.create_image(690, 492, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Perimetro, '<Button-1>', lambda e: on_Pulsador_Perimetro())
canvas.tag_bind(boton_Perimetro, '<ButtonRelease-1>', lambda e: off_Pulsador_Perimetro())

#####################################################################################################################################################

#Boton Limpieza
if plc.read("V61.0"):
    boton_Limpieza = canvas.create_image(720, 492, image=Boton2_Image, anchor='nw')
else:
    boton_Limpieza = canvas.create_image(720, 492, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_Limpieza, '<Button-1>', lambda e: on_Pulsador_Limpieza())

#####################################################################################################################################################

#Boton Checkin OK
boton_CheckinOK = canvas.create_image(45, 457, image=Boton3_Image, anchor='nw')
canvas.tag_bind(boton_CheckinOK, '<Button-1>', lambda e: on_Checkin_ok())
canvas.tag_bind(boton_CheckinOK, '<ButtonRelease-1>', lambda e: off_Checkin_ok())

#####################################################################################################################################################

#Boton Checkout Ok
boton_CheckoutOK = canvas.create_image(45, 488, image=Boton_Image, anchor='nw')
canvas.tag_bind(boton_CheckoutOK, '<Button-1>', lambda e: on_Checkout_ok())
canvas.tag_bind(boton_CheckoutOK, '<ButtonRelease-1>', lambda e: off_Checkout_ok())


#####################################################################################################################################################

#Selector Limpieza
selector_Limpieza = canvas.create_image(45, 520, image=SelectorOff, anchor='nw')
canvas.tag_bind(selector_Limpieza, '<Button-1>', lambda e: on_Limpieza())

#####################################################################################################################################################

#Portal Abriendose
portal_Abriendose = canvas.create_image(1680, 280, image="", anchor='nw')

#####################################################################################################################################################

#Luz Perimetro

luz_perimetro = canvas.create_image(298, 77, image=white_Light_off_Image, anchor=tk.CENTER)

#####################################################################################################################################################

#Luz Blanca
luz_blanca = canvas.create_image(351, 110, image=white_Light_off_Image, anchor=tk.CENTER)

#####################################################################################################################################################

#Sensor Portal Cerrado
if plc.read("V90.0"):
    sensor_cerrado = canvas.create_image(1800, 430, image=Sensor_Image, anchor=tk.CENTER)
else:
    sensor_cerrado = canvas.create_image(1800, 430, image=Sensor2_Image, anchor=tk.CENTER)
canvas.tag_bind(sensor_cerrado, '<Button-1>', lambda e: on_sensor_cerrado())

#####################################################################################################################################################

#Sensor Portal Abierto
if plc.read("V90.1"):
    sensor_abierto = canvas.create_image(1800, 120, image=Sensor_Image, anchor=tk.CENTER)
else:
    sensor_abierto = canvas.create_image(1800, 120, image=Sensor2_Image, anchor=tk.CENTER)
canvas.tag_bind(sensor_abierto, '<Button-1>', lambda e: on_sensor_abierto())

#####################################################################################################################################################

#Sensor Puerta Abierta
if plc.read("V90.2"):
    sensor_puerta = canvas.create_image(895, 180, image=Sensor3_Image, anchor=tk.CENTER)
else:
    sensor_puerta = canvas.create_image(895, 180, image=Sensor4_Image, anchor=tk.CENTER)
canvas.tag_bind(sensor_puerta, '<Button-1>', lambda e: on_sensor_puerta())

#####################################################################################################################################################

#Puerta
Puerta = canvas.create_image(890, 100, anchor=tk.CENTER)

#####################################################################################################################################################

#Portal
Portal = canvas.create_image(1780, 280, anchor=tk.CENTER)

#####################################################################################################################################################

#Luz Estados
luz_estados = canvas.create_image(20, 120, image="", anchor=tk.CENTER)

#####################################################################################################################################################

#Texto Exterior
Cuadrado_Texto = canvas.create_rectangle(920, 210, 1020, 240, fill='lightgrey')
Texto_Exterior = canvas.create_text(970, 225, text="", fill="black")

#####################################################################################################################################################

#Usuario
Usuario = canvas.create_image(-100, 0, image=Usuario_Image, anchor=tk.CENTER)

#####################################################################################################################################################

#Trabajador
Trabajador = canvas.create_image(-100, 0, image=Trabajador_Image, anchor=tk.CENTER)

#####################################################################################################################################################

#Actualizador de estados
actualizar()

#####################################################################################################################################################

#Main
root.mainloop()