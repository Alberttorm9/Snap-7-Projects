import requests
import os
import re
import xml.etree.ElementTree as ET
import configparser
import tkinter as tk

config = configparser.ConfigParser()
config.read(os.path.abspath("Config.ini"))


def mostrar_mensaje(status):
    ventana = tk.Tk()
    ventana.title("Status")

    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()

    x_pos = ancho_pantalla // 2 - 100
    y_pos = altura_pantalla // 2 - 100
    ventana.geometry('300x250+{}+{}'.format(x_pos, y_pos))

    ventana.overrideredirect(True)

    marco = tk.Frame(ventana, bg="white")
    marco.pack(expand=True, fill="both")

    mensaje = tk.Label(marco, text=f"Puerta {door_id} {status}", justify="center")
    mensaje.pack(expand=True, fill="both")

    canvas = tk.Canvas(ventana, width=50, height=50)
    if status == "DOOR_CLOSED":
        canvas.create_rectangle(5, 5, 45, 45, fill="red")
    else:
        canvas.create_rectangle(5, 5, 45, 45, fill="green")
    canvas.pack()

    ventana.after(2000, ventana.destroy)

    ventana.mainloop()



user = str(config["TESA"]["test_user"])
password =str(config["TESA"]["test_pass"])
door_id = str(config["TESA"]["puerta_1"])
host = str(config["TESA"]["IP"])
service = 'DoorsWebService'
body_close_door = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
xmlns:soap="http://soap.ws.ts1000.tesa.es/">
 <soapenv:Header/>
 <soapenv:Body>
 <soap:doorDiagnostic>
 <operatorName>{}</operatorName>
 <operatorPassword>{}</operatorPassword>
 <doorId>{}</doorId>
 </soap:doorDiagnostic>
 </soapenv:Body>
</soapenv:Envelope>
""".format(user, password, door_id)
url = f"https://{host}:8181/TesaHotelPlatform/{service}"   
headers = {'Content-Type': 'text/xml'}
try:
    response = requests.post(url, data=body_close_door, headers=headers, verify=False)
    root = ET.fromstring(response.content)
    door_status = re.search(r'<physicalState>(.*?)</physicalState>', str(response.content))
    mostrar_mensaje(door_status.group(1))
except Exception as e:
    print(e)
