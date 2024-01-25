import tkinter as tk
from tkinter import ttk
import pyodbc
import csv
import os
from datetime import datetime

# Conexión a la base de datos
server = 'LAPTOP-3UQV2BFJ\\SQLEXPRESS' 
database = 'Motel_Panamá' 
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

def exportar_informacion(tabla, desde, hasta):
    cursor = conn.cursor()
    query = "SELECT * FROM {} WHERE Time_Stamp >= ? AND Time_Stamp <= ?".format(tabla)
    cursor.execute(query, desde, hasta)
    rows = cursor.fetchall()

    carpeta_exports = 'Exports'
    
    if not os.path.exists(carpeta_exports):
        os.makedirs(carpeta_exports)
    
    archivo_csv = os.path.join(carpeta_exports, '{} {}.csv'.format(tabla,datetime.now().strftime('%d-%m-%y')))
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Interfaz de usuario
root = tk.Tk()
root.title("Exportar Información")

def establecer_fecha_actual():
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    to_entry.delete(0, 'end')
    to_entry.insert(0, fecha_actual)

def exportar():
    tabla = tabla_combobox.get()
    desde = from_entry.get()
    hasta = to_entry.get()
    exportar_informacion(tabla, desde, hasta)


fecha_actual_button = ttk.Button(root, text="Fecha actual", command=establecer_fecha_actual)
fecha_actual_button.grid(row=2, column=2)

tabla_label = ttk.Label(root, text="Tabla:")
tabla_label.grid(row=0, column=0)
tabla_combobox = ttk.Combobox(root, values=["Tiempo_Limpiando_Habitacion_1", "Tiempo_Limpiando_Habitacion_2", "Reportes"])
tabla_combobox.grid(row=0, column=1)

from_label = ttk.Label(root, text="Desde:")
from_label.grid(row=1, column=0)
from_entry = ttk.Entry(root)
from_entry.grid(row=1, column=1)

to_label = ttk.Label(root, text="Hasta:")
to_label.grid(row=2, column=0)
to_entry = ttk.Entry(root)
to_entry.grid(row=2, column=1)

export_button = ttk.Button(root, text="Exportar", command=exportar)
export_button.grid(row=3, columnspan=2)

root.mainloop()