import pyodbc
import configparser
import tkinter as tk
import pandas as pd
from pandastable import Table

# Cargar la configuración
config = configparser.ConfigParser()
config.read('config.ini')

# Conexión a la base de datos
server = str(config["DB"]["DBSERVER"])
database = str(config["DB"]["DBNAME"])
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

# Crear la ventana de la aplicación
window = tk.Tk()
window.title("Lector de base de datos")
window.geometry('800x600')  # Establece el tamaño de la ventana

frame = tk.Frame(window)
frame.pack(fill='both', expand=True)  # Asegura que el marco se expanda con la ventana

def read_db():
    cursor = conn.cursor()
    cursor.execute("SELECT Ev_Time, Ev_Message FROM EVENTHISTORY,ALARMHISTORY") 
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)
    df = df.infer_objects()  # Evita la advertencia FutureWarning
    pd.set_option('future.no_silent_downcasting', True)
    table = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
    table.show()

# Crear el botón de actualización
update_button = tk.Button(window, text="Actualizar", command=read_db)
update_button.pack()

# Iniciar la aplicación
window.mainloop()
