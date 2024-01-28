import tkinter as tk
from tkinter import PhotoImage, ttk 
from PIL import Image, ImageTk
import pyodbc
import os
import re
import sys
import configparser
from datetime import datetime, date, timedelta
import openpyxl
from openpyxl.styles import Font

#Configparser
config = configparser.ConfigParser()
config.read(os.path.abspath("Config.ini"))

#Geometry
ScreenHeight = int(config["GEOMETRIA"]["ALTO"])
ScreenWidth = int(config["GEOMETRIA"]["ANCHO"])

# Conexión a la base de datos
server = str(config["DB"]["DBSERVER"]) 
database = str(config["DB"]["DBNAME"]) 
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

def set_actual_date(type):
    ActualDate= datetime.now().strftime('%Y-%m-%d')
    if type=="Reports":
        ToEntryReports.delete(0, 'end')
        ToEntryReports.insert(0, ActualDate)
    elif type=="Exits":
        ToEntryExits.delete(0, 'end')
        ToEntryExits.insert(0, ActualDate)
    elif type=="Habs":
        ToEntryHabs.delete(0, 'end')
        ToEntryHabs.insert(0, ActualDate)

def export_month(type):
    ActualDate= datetime.now().strftime('%Y-%m-%d')
    first_day_of_month = date.today().replace(day=1)
    if type=="Reports":
        FromEntryReports.delete(0, 'end')
        FromEntryReports.insert(0, first_day_of_month)
        ToEntryReports.delete(0, 'end')
        ToEntryReports.insert(0, ActualDate)
    elif type=="Exits":
        FromEntryExits.delete(0, 'end')
        FromEntryExits.insert(0, first_day_of_month)
        ToEntryExits.delete(0, 'end')
        ToEntryExits.insert(0, ActualDate)
    elif type=="Habs":
        FromEntryHabs.delete(0, 'end')
        FromEntryHabs.insert(0, first_day_of_month)
        ToEntryHabs.delete(0, 'end')
        ToEntryHabs.insert(0, ActualDate)

def export_day(type):
    ActualDate= datetime.now().strftime('%Y-%m-%d')
    yesterday = datetime.now() - timedelta(days=1)
    yesterday = yesterday.strftime('%Y-%m-%d')
    if type=="Reports":
        FromEntryReports.delete(0, 'end')
        FromEntryReports.insert(0, yesterday)
        ToEntryReports.delete(0, 'end')
        ToEntryReports.insert(0, ActualDate)
    elif type=="Exits":
        FromEntryExits.delete(0, 'end')
        FromEntryExits.insert(0, yesterday)
        ToEntryExits.delete(0, 'end')
        ToEntryExits.insert(0, ActualDate)
    elif type=="Habs":
        FromEntryHabs.delete(0, 'end')
        FromEntryHabs.insert(0, yesterday)
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
root.config(bg='#505050')

# Configure the style for the buttons
style = ttk.Style()
style.configure('TButton', font=('calibri', 10, 'bold'), foreground='black')
style.configure('TLabel', font=('calibri', 10), foreground='black')
style.configure('TEntry', font=('calibri', 10), foreground='black')

text_font = ('Helvetica', 12, 'bold')
title_font = ('Helvetica', 20, 'bold')

#Frames
FrameExportaciones = tk.Frame(root, width=int(ScreenWidth/2), height=int(ScreenHeight/2), bg= '#505050')
FrameExportReports = tk.Frame(root, bg= '#505050')
FrameExportExit = tk.Frame(root, bg= '#505050')
FrameExportHabs = tk.Frame(root, bg= '#505050')



#Scree Gometry
ScreeGometry = f'{ScreenWidth}x{ScreenHeight}+{int((root.winfo_screenwidth() / 2) - (ScreenWidth / 2))}+{int((root.winfo_screenheight() / 2) - (ScreenHeight / 2))}'
root.geometry(ScreeGometry)
root.overrideredirect(True)
root.attributes("-topmost", True)

#Close App
x_photo = PhotoImage(file=os.path.abspath("x_button.png"))
SysCloseButton = tk.Button(root, image=x_photo, borderwidth=0, bg= '#505050', command=sys.exit)
SysCloseButton.place(relx=1, x=0, y=0, anchor='ne')

#Go Back
back_phooto = PhotoImage(file=os.path.abspath("Back_Button.png"))
GoBackButton = tk.Button(root, image=back_phooto, borderwidth=0, bg= '#505050', command=GoBack)

#Initial Frame
FrameExportaciones.place(relx=0.5, rely=0.5, anchor='center')

#####################################################################################################################################################

#Open Reports
OpenFrameReportes = ttk.Button(FrameExportaciones, text="Exportar Reportes", command=show_Reports)
OpenFrameReportes.grid(row=1, column=0, padx=10, pady=10)

#To Frame Reports
LabelReports = tk.Label(FrameExportReports, text="Exportador Tabla Reportes", bg= '#505050', font=title_font, fg='white')
LabelReports.grid(row=0, columnspan=3, pady=5)

FromLabelReports = tk.Label(FrameExportReports, text="Desde:", bg= '#505050', font=text_font, fg='white')
FromLabelReports.grid(row=1, column=0)
FromEntryReports = tk.Entry(FrameExportReports, width=12, font= 10)
FromEntryReports.grid(row=1, column=1)

ToLabelReports = tk.Label(FrameExportReports, text="Hasta:", bg='#505050', font=text_font, fg='white')
ToLabelReports.grid(row=2, column=0)
ToEntryReports = tk.Entry(FrameExportReports, width=12, font= 10)
ToEntryReports.grid(row=2, column=1)

ActualDateButtonReports = ttk.Button(FrameExportReports, text="Fecha actual", command=lambda:set_actual_date(str("Reports")))
ActualDateButtonReports.grid(row=2, column=2)

#Exportar un día
ExportLastDayReportes = ttk.Button(FrameExportReports, text="Exportar Último Dia", width=17, command=lambda:export_day(str("Reports")))
ExportLastDayReportes.grid(row=1, column=4, padx=5, pady=2, sticky="w")

ExportLastMonthReportes = ttk.Button(FrameExportReports, text="Exportar Último Mes", width=17, command=lambda:export_month(str("Reports")))
ExportLastMonthReportes.grid(row=2, column=4, padx=5, pady=2, sticky="w")

ExportButtonReports = ttk.Button(FrameExportReports, text="Exportar", command=lambda:export(str("Reports")))
ExportButtonReports.grid(row=3, column=1, columnspan=1, pady=(10, 0), sticky="nsew")

#####################################################################################################################################################

# Update the widget styles
OpenFrameExit = ttk.Button(FrameExportaciones, text="Exportar Salidas Del Sistema", command=show_Exit)
OpenFrameExit.grid(row=1, column=1, padx=10, pady=10)

#To Frame Exits
LabelExits = tk.Label(FrameExportExit, text="Exportador Tabla Reportes", bg= '#505050', font=title_font, fg='white')
LabelExits.grid(row=0, columnspan=3, pady=5)

FromLabelExits = tk.Label(FrameExportExit, text="Desde:", bg= '#505050', font=text_font, fg='white')
FromLabelExits.grid(row=1, column=0)
FromEntryExits = tk.Entry(FrameExportExit, width=12, font= 10)
FromEntryExits.grid(row=1, column=1)

ToLabelExits = tk.Label(FrameExportExit, text="Hasta:", bg='#505050', font=text_font, fg='white')
ToLabelExits.grid(row=2, column=0)
ToEntryExits = tk.Entry(FrameExportExit, width=12, font= 10)
ToEntryExits.grid(row=2, column=1)

ActualDateButtonExits = ttk.Button(FrameExportExit, text="Fecha actual", command=set_actual_date)
ActualDateButtonExits.grid(row=2, column=2)

ExportButtonExits = ttk.Button(FrameExportExit, text="Exportar", command=lambda:export(str("Exits")))
ExportButtonExits.grid(row=3, column=1, columnspan=1, pady=(10, 0), sticky="nsew")

#####################################################################################################################################################

#Open Habs
OpenFrameHabs = ttk.Button(FrameExportaciones, text="Exportar Limpieza Habitaciones", command=show_Habs)
OpenFrameHabs.grid(row=1, column=2, padx=10, pady=10)

#To Frame Habs
LabelHabs = tk.Label(FrameExportHabs, text="Exportador Tabla Habitaciones", bg= '#505050', font=title_font, fg='white')
LabelHabs.grid(row=0, columnspan=6, pady=5)

TableHabs = tk.Label(FrameExportHabs, text="Tabla:", bg= '#505050', font=text_font, fg='white')
TableHabs.grid(row=1, column=1)
with open('archivo_valores.txt', 'r') as file:
    ListHabs = file.readlines()
    ListHabs = [valor.strip() for valor in ListHabs]
TableComboxHabs = ttk.Combobox(FrameExportHabs, values=ListHabs, width=31)
TableComboxHabs.grid(row=1, column=2, padx=2)

FromLabelHabs = tk.Label(FrameExportHabs, text="Desde:", bg= '#505050', font=text_font, fg='white')
FromLabelHabs.grid(row=1, column=3)
FromEntryHabs = tk.Entry(FrameExportHabs)
FromEntryHabs.grid(row=1, column=4)

ToLabelHabs = tk.Label(FrameExportHabs, text="Hasta:", bg= '#505050', font=text_font, fg='white')
ToLabelHabs.grid(row=2, column=3)
ToEntryHabs = tk.Entry(FrameExportHabs)
ToEntryHabs.grid(row=2, column=4)

ActualDateButtonHabs = ttk.Button(FrameExportHabs, text="Fecha actual", command=set_actual_date)
ActualDateButtonHabs.grid(row=2, column=5, padx=10)

ExportButtonHabs = ttk.Button(FrameExportHabs, text="Exportar", command=lambda:export(str("Habs")))
ExportButtonHabs.grid(row=4, columnspan=6, pady=10)

#####################################################################################################################################################

root.mainloop()