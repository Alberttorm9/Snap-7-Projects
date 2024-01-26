import tkinter as tk
from tkinter import ttk, PhotoImage
import pyodbc
import csv
import os
import re
import sys
import configparser
from datetime import datetime

#Configparser
config = configparser.ConfigParser()
config.read(os.path.abspath("Config.ini"))

#Geometry
ScreenHeight = int(config["GEOMETRIA"]["ALTO"])
ScreenWidth = int(config["GEOMETRIA"]["ANCHO"])

# Conexión a la base de datos
server = 'LAPTOP-3UQV2BFJ\\SQLEXPRESS' 
database = 'Motel_Panamá' 
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

def export_Info(tabla, desde, hasta, type):
    cursor = conn.cursor()
    if type=="Reports":
        query = f"SELECT Reportes_Texto_Reporte,Reportes_Hora_Reporte,Reportes_Numero_Reporte,Reportes_Hora_Real_Reporte,Reportes_Numero_Real_Reporte FROM {tabla} WHERE Time_Stamp BETWEEN '{desde}' AND '{hasta}'"
        carpeta_exports = fr'{str(config["RUTA"]["REPORTES"])}'
        encabezados = ['Texto Del Reporte','Hora Del Reporte','Numero Del Reporte','Hora Real Del Reporte','Numero Real Del Reporte']
    elif type =="Exits":
        query = f"SELECT Now_Local,sys_On_Off FROM {tabla} WHERE Time_Stamp BETWEEN '{desde}' AND '{hasta}'"
        carpeta_exports = fr'{str(config["RUTA"]["SALIDAS"])}'
        encabezados = ['Hora De Accion','Tipo De Accion']
    elif type=="Habs":
        NumeroHab = re.findall(r'\d+', tabla)  # Encuentra todos los dígitos en la cadena de texto
        query = f"SELECT Time_Stamp,Hab_{int(NumeroHab[0])-1}_Tiempo_Limpiando FROM {tabla} WHERE Time_Stamp BETWEEN '{desde}' AND '{hasta}'"
        carpeta_exports = fr'{str(config["RUTA"]["HABITACIONES"])}'
        encabezados = ['Hora Terminada',f'Tiempo Limpiando Habitación {int(NumeroHab[0])}']
    print(query+"\n\n")
    cursor.execute(query)
    rows = cursor.fetchall()
    
    if not os.path.exists(carpeta_exports):
        os.makedirs(carpeta_exports)
    
    archivo_csv = os.path.join(carpeta_exports, '{} {}.csv'.format(tabla,datetime.now().strftime('%d-%m-%y')))
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer = csv.writer(file)
        writer.writerow(encabezados)  # Escribir los encabezados personalizados en la primera línea
        writer.writerows(rows)

def set_actual_date():
    ActualDate= datetime.now().strftime('%Y-%m-%d')
    ToEntryReports.delete(0, 'end')
    ToEntryReports.insert(0, ActualDate)
    ToEntryExits.delete(0, 'end')
    ToEntryExits.insert(0, ActualDate)
    ToEntryHabs.delete(0, 'end')
    ToEntryHabs.insert(0, ActualDate)

def export(type):
    if type=="Reports":
        table = "Reportes"
        since = FromEntryReports.get()
        till = ToEntryReports.get()
    elif type=="Exits":
        table = "Salida_De_Programa"
        since = FromEntryExits.get()
        till = ToEntryExits.get()
    elif type=="Habs":
        table = TableComboxHabs.get()
        since = FromEntryHabs.get()
        till = ToEntryHabs.get()
    
    
    export_Info(table, since, till, type)




def show_Reports():
    FrameExportaciones.place_forget()
    FrameExportReports.place(relx=0.5, rely=0.5, anchor='center')

def show_Exit():
    FrameExportaciones.place_forget()
    FrameExportExit.place(relx=0.5, rely=0.5, anchor='center')

def show_Habs():
    FrameExportaciones.place_forget()
    FrameExportHabs.place(relx=0.5, rely=0.5, anchor='center')


# Interfaz de usuario
root = tk.Tk()
root.title("Exportar Información")

#TkStyle
Tkstyle = ttk.Style()
Tkstyle.configure('Custom.TButton', font=('Helvetica', 12), padding=10)

#Frames
FrameExportaciones = tk.Frame(root, width=int(ScreenWidth/2), height=int(ScreenHeight/2))
FrameExportReports = tk.Frame(root)
FrameExportExit = tk.Frame(root)
FrameExportHabs = tk.Frame(root)

#Scree Gometry
ScreeGometry = f'{ScreenWidth}x{ScreenHeight}+{int((root.winfo_screenwidth() / 2) - (ScreenWidth / 2))}+{int((root.winfo_screenheight() / 2) - (ScreenHeight / 2))}'
root.geometry(ScreeGometry)
root.overrideredirect(True)
root.attributes("-topmost", True)

#Close App
x_photo = PhotoImage(file=os.path.abspath("x_button.png"))
SysCloseButton = tk.Button(root, bg='lightgrey', image=x_photo, borderwidth=0, highlightthickness=0,  command=sys.exit)
SysCloseButton.place(relx=1, x=0, y=0, anchor='ne')


#Initial Frame
FrameExportaciones.place(relx=0.5, rely=0.5, anchor='center')

#####################################################################################################################################################

#Open Reports
OpenFrameReportes = ttk.Button(FrameExportaciones, text="Exportar Reportes", command=show_Reports, style='Custom.TButton')
OpenFrameReportes.grid(row=1, column=0, padx=10, pady=10)
#To Frame Reports
FromLabelReports = ttk.Label(FrameExportReports, text="Desde:")
FromLabelReports.grid(row=1, column=1)
FromEntryReports = ttk.Entry(FrameExportReports)
FromEntryReports.grid(row=1, column=2)

ToLabelReports = ttk.Label(FrameExportReports, text="Hasta:")
ToLabelReports.grid(row=2, column=1)
ToEntryReports = ttk.Entry(FrameExportReports)
ToEntryReports.grid(row=2, column=2)

ActualDateButtonReports = ttk.Button(FrameExportReports, text="Fecha actual", command=set_actual_date)
ActualDateButtonReports.grid(row=2, column=3)

ExportButtonReports = ttk.Button(FrameExportReports, text="Exportar", command=lambda:export(str("Reports")))
ExportButtonReports.grid(row=3, columnspan=3)

#####################################################################################################################################################

#Open System Exits
OpenFrameExit = ttk.Button(FrameExportaciones, text="Exportar Salidas Del Sistema", command=show_Exit, style='Custom.TButton')
OpenFrameExit.grid(row=1, column=1, padx=10, pady=10)

#To Frame Exits
FromLabelExits = ttk.Label(FrameExportExit, text="Desde:")
FromLabelExits.grid(row=1, column=1)
FromEntryExits = ttk.Entry(FrameExportExit)
FromEntryExits.grid(row=1, column=2)

ToLabelExits = ttk.Label(FrameExportExit, text="Hasta:")
ToLabelExits.grid(row=2, column=1)
ToEntryExits = ttk.Entry(FrameExportExit)
ToEntryExits.grid(row=2, column=2)

ActualDateButtonExits = ttk.Button(FrameExportExit, text="Fecha actual", command=set_actual_date)
ActualDateButtonExits.grid(row=2, column=3)

ExportButtonExits = ttk.Button(FrameExportExit, text="Exportar", command=lambda:export(str("Exits")))
ExportButtonExits.grid(row=3, columnspan=3)

#####################################################################################################################################################

#Open Habs
OpenFrameHabs = ttk.Button(FrameExportaciones, text="Exportar Limpieza Habitaciones", command=show_Habs, style='Custom.TButton')
OpenFrameHabs.grid(row=1, column=2, padx=10, pady=10)

#To Frame Habs
TableHabs = ttk.Label(FrameExportHabs, text="Tabla:")
TableHabs.grid(row=1, column=1)
with open('archivo_valores.txt', 'r') as file:
    ListHabs = file.readlines()
    ListHabs = [valor.strip() for valor in ListHabs]
TableComboxHabs = ttk.Combobox(FrameExportHabs, values=ListHabs, width=31)
TableComboxHabs.grid(row=1, column=2, padx=2)

FromLabelHabs = ttk.Label(FrameExportHabs, text="Desde:")
FromLabelHabs.grid(row=1, column=3)
FromEntryHabs = ttk.Entry(FrameExportHabs)
FromEntryHabs.grid(row=1, column=4)

ToLabelHabs = ttk.Label(FrameExportHabs, text="Hasta:")
ToLabelHabs.grid(row=2, column=3)
ToEntryHabs = ttk.Entry(FrameExportHabs)
ToEntryHabs.grid(row=2, column=4)

ActualDateButtonHabs = ttk.Button(FrameExportHabs, text="Fecha actual", command=set_actual_date)
ActualDateButtonHabs.grid(row=2, column=5)

ExportButtonHabs = ttk.Button(FrameExportHabs, text="Exportar", command=lambda:export(str("Habs")))
ExportButtonHabs.grid(row=4, columnspan=6)

#####################################################################################################################################################

root.mainloop()