import tkinter as tk
from tkinter import ttk, PhotoImage, Tk, Frame, Label
from PIL import Image, ImageTk
import pyodbc
import os
import re
import sys
import configparser
from datetime import datetime
import openpyxl
from openpyxl.styles import Font

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
        query = f"SELECT Reportes_Texto_Reporte, Reportes_Hora_Reporte, Reportes_Numero_Reporte, Reportes_Hora_Real_Reporte, Reportes_Numero_Real_Reporte FROM {tabla} WHERE Time_Stamp >= '{desde}' AND Time_Stamp <= '{hasta} 23:59:59.000000'"
        carpeta_exports = str(config["RUTA"]["REPORTES"])
        encabezados = ('Texto Del Reporte', 'Hora Del Reporte', 'Numero Del Reporte', 'Hora Real Del Reporte', 'Numero Real Del Reporte')
        CantidadValores = 5
    elif type =="Exits":
        query = f"SELECT Now_Local, sys_On_Off FROM {tabla} WHERE Time_Stamp >= '{desde}' AND Time_Stamp <= '{hasta} 23:59:59.000000'"
        carpeta_exports = str(config["RUTA"]["SALIDAS"])
        encabezados = ['Hora De Accion', 'Tipo De Accion']
        CantidadValores = 2
    elif type=="Habs":
        NumeroHab = re.findall(r'\d+', tabla)  # Encuentra todos los dígitos en la cadena de texto
        query = f"SELECT Time_Stamp, Hab_{int(NumeroHab[0])-1}_Tiempo_Limpiando FROM {tabla} WHERE Time_Stamp >= '{desde}' AND Time_Stamp <= '{hasta} 23:59:59.000000'"
        carpeta_exports = str(config["RUTA"]["HABITACIONES"])
        encabezados = ['Hora Terminada', f'Tiempo Limpiando Habitación {int(NumeroHab[0])}']
        CantidadValores = 2

    print(query + "\n\n")
    cursor.execute(query)
    rows = cursor.fetchall()
    rows = [(re.sub(r"[\(\)]", "", item) if isinstance(item, str) else item) for row in rows for item in row]

    if not os.path.exists(carpeta_exports):
        os.makedirs(carpeta_exports)


    exportar_excel(rows, encabezados, CantidadValores, carpeta_exports, tabla)

def exportar_excel(rows, encabezados,CantidadValores, carpeta_exports, tabla):
    wb = openpyxl.Workbook()
    sheet = wb.active
    #Encabezado
    for col, encabezado in enumerate(encabezados, 1):
        sheet.cell(row=1, column=col, value=encabezado)
        sheet.cell(row=1, column=col).font = Font(bold=True)
    #Lineas
    x=0
    y=0
    for col, rowData in enumerate(rows, 1):
        y=y+1
        sheet.cell(row=x+2, column=y, value=rowData)
        if col % CantidadValores == 0:
            x=x+1
            y=0

    wb.save(f'{carpeta_exports}\{tabla} {datetime.now().strftime("%d-%m-%y")}.xlsx')

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

def GoBack():
    GoBackButton.place_forget()
    FrameExportReports.place_forget()
    FrameExportExit.place_forget()
    FrameExportHabs.place_forget()
    FrameExportaciones.place(relx=0.5, rely=0.5, anchor='center')

def show_Reports():
    FrameExportaciones.place_forget()
    FrameExportReports.place(relx=0.5, rely=0.5, anchor='center')
    GoBackButton.place(relx=0, x=0, y=0, anchor='nw')

def show_Exit():
    FrameExportaciones.place_forget()
    FrameExportExit.place(relx=0.5, rely=0.5, anchor='center')
    GoBackButton.place(relx=0, x=0, y=0, anchor='nw')

def show_Habs():
    FrameExportaciones.place_forget()
    FrameExportHabs.place(relx=0.5, rely=0.5, anchor='center')
    GoBackButton.place(relx=0, x=0, y=0, anchor='nw')


# Interfaz de usuario
root = tk.Tk()
root.title("Exportar Información")
imagen_fondo = Image.open("fondo.png")
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
etiqueta_fondo = Label(root, image=imagen_fondo)
etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#TkStyle
Tkstyle = ttk.Style()
Tkstyle.configure('Custom.TButton', font=('Helvetica', 12), padding=10)
Tkstyle.configure('Title.TLabel', font=('Arial', 14, 'bold'))
Tkstyle.configure('Invisible.TButton', borderwidth=0, borderheight=0, highlightthickness=0, relief="flat")
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
SysCloseButton = tk.Button(root, image=x_photo, borderwidth=0, highlightthickness=0,  command=sys.exit)
SysCloseButton.place(relx=1, x=0, y=0, anchor='ne')

#Go Back
back_phooto = PhotoImage(file=os.path.abspath("Back_Button.png"))
GoBackButton = ttk.Button(root, image=back_phooto, style='Invisible.TButton',command=GoBack)

#Initial Frame
FrameExportaciones.place(relx=0.5, rely=0.5, anchor='center')

#####################################################################################################################################################

#Open Reports
OpenFrameReportes = ttk.Button(FrameExportaciones, text="Exportar Reportes", command=show_Reports, style='Custom.TButton')
OpenFrameReportes.grid(row=1, column=0, padx=10, pady=10)

#To Frame Reports
LabelReports = ttk.Label(FrameExportReports, text="Exportador Tabla Reportes", style='Title.TLabel')
LabelReports.grid(row=0, columnspan=3, pady=5)

FromLabelReports = ttk.Label(FrameExportReports, text="Desde:")
FromLabelReports.grid(row=1, column=0)
FromEntryReports = ttk.Entry(FrameExportReports)
FromEntryReports.grid(row=1, column=1)

ToLabelReports = ttk.Label(FrameExportReports, text="Hasta:")
ToLabelReports.grid(row=2, column=0)
ToEntryReports = ttk.Entry(FrameExportReports)
ToEntryReports.grid(row=2, column=1)

ActualDateButtonReports = ttk.Button(FrameExportReports, text="Fecha actual", command=set_actual_date)
ActualDateButtonReports.grid(row=2, column=2)

ExportButtonReports = ttk.Button(FrameExportReports, text="Exportar", command=lambda:export(str("Reports")))
ExportButtonReports.grid(row=3, columnspan=2)

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