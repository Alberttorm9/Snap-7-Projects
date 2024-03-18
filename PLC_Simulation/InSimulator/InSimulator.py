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


root = tk.Tk()

SensorPortalAbriendo = tk.Button(root, text= "Sensor Abriendo", command=SensorPortalAbriendoAct)
SensorPortalAbriendo.pack()
SensorPortalCerrando = tk.Button(root, text= "Sensor Cerrando", command=SensorPortalCerrandoAct)
SensorPortalCerrando.pack()
ActivarAlarmaPortal = tk.Button(root, text= "Activar Alarma", command=ActivarAlarmaPortalAct)
ActivarAlarmaPortal.pack()
SelectorLimpieza = tk.Button(root, text= "Selector Limpieza", command=SelectorLimpiezaAct)
SelectorLimpieza.pack()
CheckinOK = tk.Button(root, text= "Checkin OK", command=CheckinOKAct)
CheckinOK.pack()
CheckoutOK = tk.Button(root, text= "Checkout OK", command=CheckoutOKAct)
CheckoutOK.pack()
SolicitudCheckin = tk.Button(root, text= "Solicitud Checkin", command=SolicitudCheckinAct)
SolicitudCheckin.pack()
RGB = tk.Button(root, text= "RGB", command=RGBAct)
RGB.pack()
LuzBlanca = tk.Button(root, text= "Luz Blanca", command=LuzBlancaAct)
LuzBlanca.pack()
SolicitudCheckout = tk.Button(root, text= "Solicitud Checkout", command=SolicitudCheckoutAct)
SolicitudCheckout.pack()
SensorPuertaEntrada = tk.Button(root, text= "Sensor Puerta Entrada", command=SensorPuertaEntradaAct)
SensorPuertaEntrada.pack()

