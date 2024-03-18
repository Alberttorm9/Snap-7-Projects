import tkinter as tk
import snap7

plc = snap7.logo.Logo()
plc.connect("192.168.30.101", 0, 1)

def SensorPortalAbriendoAct():
    if plc.read("V60.0"):
        plc.write("V60.0", 0)
        plc.write("V60.2", 0)
    else:
        plc.write("V60.0", 1)
        plc.write("V60.2", 1)


def SensorPortalCerrandoAct():
    if plc.read("V60.1"):
        plc.write("V60.1", 0)
        plc.write("V60.2", 0)

    else:
        plc.write("V60.1", 1)
        plc.write("V60.2", 1)

def ActivarAlarmaPortalAct():
    if plc.read("V60.2"):
        plc.write("V60.2", 0)
    else:
        plc.write("V60.2", 1)

def SelectorLimpiezaAct():
    if plc.read("V60.3"):
        plc.write("V60.3", 0)
    else:
        plc.write("V60.3", 1)

def CheckinOKAct():
    if plc.read("V60.4"):
        plc.write("V60.4", 0)
    else:
        plc.write("V60.4", 1)

def CheckoutOKAct():
    if plc.read("V60.5"):
        plc.write("V60.5", 0)
    else:
        plc.write("V60.5", 1)

def SolicitudCheckinAct():
    if plc.read("V60.6"):
        plc.write("V60.6", 0)
    else:
        plc.write("V60.6", 1)

def RGBAct():
    if plc.read("V60.7"):
        plc.write("V60.7", 0)
    else:
        plc.write("V60.7", 1)

def LuzBlancaAct():
    if plc.read("V70.0"):
        plc.write("V70.0", 0)
    else:
        plc.write("V70.0", 1)


def SolicitudCheckoutAct():
    if plc.read("V70.1"):
        plc.write("V70.1", 0)
    else:
        plc.write("V70.1", 1)

def SensorPuertaEntradaAct():
    if plc.read("V70.2"):
        plc.write("V70.2", 0)
    else:
        plc.write("V70.2", 1)

def PulsadorGarajeAct():
    if plc.read("V70.3"):
        plc.write("V70.3", 0)
    else:
        plc.write("V70.3", 1)

def RectonnectAct():
    if plc.get_connected:
        plc.disconnect()
        plc.connect("192.168.30.101", 0, 1)
    else:
        plc.connect("192.168.30.101", 0, 1)


def actualizar():

    if plc.read("V12.1"):
        PuertaPeatonal.config(text="Puerta Peatonal: " + "1")
    else:
        PuertaPeatonal.config(text="Puerta Peatonal: " + "0")
    
    if plc.read("V80.0"):
        AbriendoPortal.config(text="Portal Abrir: " + "1")
    else:
        AbriendoPortal.config(text="Portal Abrir: " + "0")
    
    if plc.read("V80.1"):
        CerrandoPortal.config(text="Portal Cerrar: " + "1")
    else:
        CerrandoPortal.config(text="Portal Cerrar: " + "0")

    root.after(100, actualizar)

root = tk.Tk()

SensorPortalAbriendo = tk.Button(root, text= "Sensor Abriendo", command=SensorPortalAbriendoAct)
SensorPortalAbriendo.grid(row=1,column=1)
SensorPortalCerrando = tk.Button(root, text= "Sensor Cerrando", command=SensorPortalCerrandoAct)
SensorPortalCerrando.grid(row=2,column=1)
ActivarAlarmaPortal = tk.Button(root, text= "Activar Alarma", command=ActivarAlarmaPortalAct)
ActivarAlarmaPortal.grid(row=3,column=1)
SelectorLimpieza = tk.Button(root, text= "Selector Limpieza", command=SelectorLimpiezaAct)
SelectorLimpieza.grid(row=4,column=1)
CheckinOK = tk.Button(root, text= "Checkin OK", command=CheckinOKAct)
CheckinOK.grid(row=5,column=1)
CheckoutOK = tk.Button(root, text= "Checkout OK", command=CheckoutOKAct)
CheckoutOK.grid(row=6,column=1)
SolicitudCheckin = tk.Button(root, text= "Solicitud Checkin", command=SolicitudCheckinAct)
SolicitudCheckin.grid(row=7,column=1)
RGB = tk.Button(root, text= "RGB", command=RGBAct)
RGB.grid(row=8,column=1)
LuzBlanca = tk.Button(root, text= "Luz Blanca", command=LuzBlancaAct)
LuzBlanca.grid(row=9,column=1)
SolicitudCheckout = tk.Button(root, text= "Solicitud Checkout", command=SolicitudCheckoutAct)
SolicitudCheckout.grid(row=10,column=1)
SensorPuertaEntrada = tk.Button(root, text= "Sensor Puerta Entrada", command=SensorPuertaEntradaAct)
SensorPuertaEntrada.grid(row=11,column=1)
PulsadorGaraje = tk.Button(root, text= "Pulsador Garaje", command=PulsadorGarajeAct)
PulsadorGaraje.grid(row=12,column=1)
Rectonnect = tk.Button(root, text= "Rectonnect", command=RectonnectAct)
Rectonnect.grid(row=13,column=1)

PuertaPeatonal = tk.Label(root)
PuertaPeatonal.grid(row=1,column=2)

AbriendoPortal = tk.Label(root)
AbriendoPortal.grid(row=2,column=2)

CerrandoPortal = tk.Label(root)
CerrandoPortal.grid(row=3,column=2)

actualizar()

root.mainloop()