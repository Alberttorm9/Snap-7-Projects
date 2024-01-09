import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import sys
import configparser
import re
import os
import PySimpleGUI as sg
from cryptography.fernet import Fernet
import requests

#Configparser
config = configparser.ConfigParser()
config.read(os.path.abspath("Config.ini"))

# Encripter
def encriptar_contraseña(contraseña):
    clave = Fernet.generate_key()
    f = Fernet(clave)
    contraseña_encriptada = f.encrypt(contraseña.encode())
    with open('clave.key', 'wb') as archivo_clave:
        archivo_clave.write(clave)
    return contraseña_encriptada

# Decripter
def desencriptar_contraseña():
    with open('clave.key', 'rb') as archivo_clave:
        clave = archivo_clave.read()
    f = Fernet(clave)
    with open('contraseña_encriptada.txt', 'rb') as archivo_contraseña:
        contraseña_encriptada = archivo_contraseña.read()
    contraseña = f.decrypt(contraseña_encriptada).decode()
    return contraseña

#XML creator
def give_XML(DoorNum, Operator):
    password = desencriptar_contraseña()
    body_open_door = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:soap="http://soap.ws.ts1000.tesa.es/">
    <soapenv:Header/>
    <soapenv:Body>
    <soap:doorOpen>
    <operatorName>{}</operatorName>
    <operatorPassword>{}</operatorPassword>
    <doorName>{}</doorName>
    </soap:doorOpen>
    </soapenv:Body>
    </soapenv:Envelope>
    """.format(str(Operator), password,DoorNum)
    return(body_open_door)

#Close program
def close_window():
    sys.exit()

def door_selection(NumPuerta):
    close_button.grid(row=0, column=0, sticky="ne")
    label_door_selected.config(text="Puerta Nº " + str(NumPuerta), padx=20)
    frame_door_selected.grid()
    label_door_selected.grid(row=0, column=0)
    button_open.grid(row=1, column=0, pady=5)

def open_door(NumAbrir):
    host = str(config["TESA"]["IP"])
    service = 'DoorsWebService'
    body_open_door = give_XML(NumAbrir, str(config["TESA"]["usuario"]))
    url = f"https://{host}:8181/TesaHotelPlatform/{service}"   
    headers = {'Content-Type': 'text/xml'}
    try:
        response = requests.post(url, data=body_open_door, headers=headers, verify=False)
    except Exception:
        messagebox.showerror("Error", "ERROR EN LA IP")
        sys.exit()
    if response.status_code == 200:
        try:
            response_shown = re.search(r'<errorType>(.*?)</errorType>', str(response.content))
            if (response_shown.group(1) == "ERROR_SERVICE_AUTHENTICATION"):
                response_shown = "ERROR EN LA AUTENTICACION"
                messagebox.showerror("Error", response_shown)
            elif(response_shown.group(1) == "ERROR_OPERATION_DOOR_UNKNOWN"):
                response_shown = "PUERTA NO ENCONTRADA"
                messagebox.showerror("Error", response_shown)
            else:
                messagebox.showerror("Error", response_shown.group(1))
        except Exception:
            response_shown = re.search(r'<type>(.*?)</type>', str(response.content))
            messagebox.showinfo("Éxito", "PUERTA ABIERTA")
    else:
        response_shown = re.search(r'<errorType>(.*?)</errorType>', str(response.text))
        messagebox.showinfo("Error", response_shown.group(1))

#Root & frame creator
root = tk.Tk()
root.title("Abrir Puertas")
frame_door_selected = tk.Frame(root, bg='lightgrey')
root.config(bg='lightgrey')
root.overrideredirect(True)

#Always on top
root.attributes("-topmost", True)
root.lift()

#Hide root (temporal)
root.withdraw()
 
#Image Sources
x_photo = PhotoImage(file=os.path.abspath("x_button.png"))
door_open_photo = PhotoImage(file=os.path.abspath("Open_Door.png"))

# Widgets
close_button = tk.Button(root, bg='lightgrey', image=x_photo, borderwidth=0, highlightthickness=0,  command=close_window)
label_door_selected = tk.Label(frame_door_selected, text="", font=("Times New Roman", 24, "bold"), bg='lightgrey')
button_open = tk.Button(frame_door_selected, image=door_open_photo, borderwidth=0, highlightthickness=0, bg= 'lightgrey', command=lambda:open_door(config.get('TESA', 'Puerta_1')))


# Pass Struct check
if (os.path.exists('clave.key') or os.path.exists('contraseña_encriptada.txt')) and (not os.path.exists('clave.key') or not os.path.exists('contraseña_encriptada.txt' )):
    messagebox.showerror("ERROR", "UNA DE LAS CONTRASEÑAS NO EXISTE\n\nElimine Contraseña_Encriptada.txt y clave.key\n\nDirectorio: " + os.path.abspath("Open_Door.exe"))
    sys.exit()

# Loggin Check
if ((str(config["TESA"]["usuario"]) == "") or (not os.path.exists('clave.key'))):
    usuario = None
    contraseña = None

    layout = [
        [sg.Text('Introduce el usuario de TESA:'), sg.InputText()],
        [sg.Text('Introduce la contraseña de TESA:'), sg.InputText(password_char='*')],
        [sg.Button('Aceptar')]
    ]

    window = sg.Window('Ingreso de Usuario y Contraseña', layout)

    event, values = window.read()
    if event == 'Aceptar':
        usuario = values[0]
        contraseña = values[1]
        # Verification -> Correct imput
        if not usuario or not contraseña:
            sys.exit()
        # Verification -> User exists
        if str(config["TESA"]["usuario"]) == "":
            config.set('TESA', 'Usuario', usuario)
            with open('Config.ini', 'w') as archivo_config:
                config.write(archivo_config)
        # Verification -> Pass exists
        if not os.path.exists('clave.key'):
            contraseña_encriptada = encriptar_contraseña(contraseña)
            with open('contraseña_encriptada.txt', 'wb') as archivo_contraseña:
                archivo_contraseña.write(contraseña_encriptada)
        else:
            contraseña = desencriptar_contraseña()

    window.close()
root.deiconify()

# Verification -> User & Pass exists
if ((str(config["TESA"]["usuario"]) == "") or (not os.path.exists('clave.key'))):
    sys.exit()

# Mainloop
door_selection(str(config["TESA"]["Puerta_1"]))
root.mainloop()