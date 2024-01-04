import tkinter as tk
from tkinter import messagebox
import requests
import configparser
import re
import customtkinter as ctk

config = configparser.ConfigParser()
config.read('Config.ini')
print(config.get('Tesa', 'IP'))
def show_loggin():
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')
    frame_door_selection.grid_forget()
    frame_loggin.grid()
    label_username.grid(row=0, column=0)
    label_password.grid(row=1, column=0)
    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)
    button_login.grid(row=2, columnspan=2)
    entry_username.bind('<Return>',login)
    entry_password.bind('<Return>',login)


def login(event):
    username = entry_username.get()
    password = entry_password.get()

    # Verificar las credenciales (aquí puedes agregar tu lógica de autenticación)
    if username == "XXX" and password == "XXX":
        frame_loggin.grid_forget()
        show_door_selection()
    else:
        messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")

def show_door_selection():
    entry_door.delete(0, 'end')
    frame_door_selected.grid_forget()
    frame_door_selection.grid()
    entry_door.grid(row=1, column=0)
    button_go_selected_door.grid(row=2, column=0)
    label_door.grid(row=0,column=0)
    button_logout.grid(row = 0, column=1)
    entry_door.bind('<Return>',lambda event: door_selection(entry_door.get()))

def door_selection(NumPuerta):
    label_door_selected.config(text="La puerta seleccionada es la Nº " + str(NumPuerta))

    frame_door_selection.grid_forget()
    frame_door_selection.grid_forget()
    frame_door_selected.grid()
    label_door_selected.grid(row=0, column=1)
    button_open.grid(row=1, column=0)
    button_close.grid(row=1, column=2)
    button_go_back.grid(row=2, column=1)

def open_door():
    host = config.get('Tesa', 'IP')
    service = 'DoorsWebService'
    body_close_door = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:soap="http://soap.ws.ts1000.tesa.es/">
    <soapenv:Header/>
    <soapenv:Body>
    <soap:doorOpen>
    <operatorName>{}</operatorName>
    <operatorPassword>{}</operatorPassword>
    <doorName>{}</doorName>
    </soap:doorOpen>
    </soapenv:Body>
    </soapenv:Envelope>"
    """.format(entry_username.get(), entry_password.get(),entry_door.get())
    url = f"https://{host}:8181/TesaHotelPlatform/{service}"   
    headers = {'Content-Type': 'text/xml'}
    try:
        response = requests.post(url, data=body_close_door, headers=headers, verify=False)
    except Exception:
        messagebox.showerror("Error", "Is the ip well configured?")
    if response.status_code == 200:
        response_shown = re.search(r'<errorType>(.*?)</errorType>', str(response.content))
        messagebox.showinfo("Éxito", response_shown.group(1))
        print(response.content)
        return response.content
    else:
        response_shown = re.search(r'<errorType>(.*?)</errorType>', str(response.text))
        messagebox.showinfo("Error", response_shown.group(1))
        print(response.text)
        return None, response.text

def close_door():
    host = config.get('Tesa', 'IP')
    service = 'DoorsWebService'
    body_close_door = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:soap="http://soap.ws.ts1000.tesa.es/">
    <soapenv:Header/>
    <soapenv:Body>
    <soap:doorClose>
    <operatorName>{}</operatorName>
    <operatorPassword>{}</operatorPassword>
    <doorName>{}</doorName>
    </soap:doorClose>
    </soapenv:Body>
    </soapenv:Envelope>
    """.format(entry_username.get(), entry_password.get(),entry_door.get())


    url = f"https://{host}:8181/TesaHotelPlatform/{service}"
    headers = {'Content-Type': 'text/xml'}
    try:
        response = requests.post(url, data=body_close_door, headers=headers, verify=False)
    except Exception:
        messagebox.showerror("Error", "Is the ip well configured?")
    if response.status_code == 200:
        response_shown = re.search(r'<errorType>(.*?)</errorType>', str(response.content))
        messagebox.showinfo("Éxito", response_shown.group(1))
        print(response.content)
        return response.content
    else:
        response_shown = re.search(r'<errorType>(.*?)</errorType>', str(response.text))
        messagebox.showinfo("Error", response_shown.group(1))
        print(response.text)
        return None, response.text


# Crear la ventana principal
root = tk.Tk()
root.title("Inicio de Sesión")
frame_loggin = tk.Frame(root)
frame_door_selection = tk.Frame(root)
frame_door_selected = tk.Frame(root)

# Crear widgets
label_username = tk.Label(frame_loggin, text="Usuario:")
label_password = tk.Label(frame_loggin, text="Contraseña:")
label_door = tk.Label(frame_door_selection, text="Número de Puerta:")
entry_username = tk.Entry(frame_loggin)
entry_password = tk.Entry(frame_loggin, show="*")
button_login = tk.Button(frame_loggin, text="Iniciar Sesión", command=lambda:login(1))

entry_door = tk.Entry(frame_door_selection)
label_door = tk.Label(frame_door_selection, text="Puerta:")
button_go_selected_door = tk.Button(frame_door_selection, text="Enter", command=lambda:door_selection(entry_door.get()))
button_logout = tk.Button(frame_door_selection, text="Cerrar Sesion", command=show_loggin)

label_door_selected = tk.Label(frame_door_selected, text="")
button_open = ctk.CTkButton(frame_door_selected, text="Abrir", command=open_door)
button_close = ctk.CTkButton(frame_door_selected, text="Cerrar", command=close_door)
button_go_back = ctk.CTkButton(frame_door_selected, text="Atras", command=show_door_selection)


# Ejecutar la aplicación
show_loggin()
root.mainloop()