import pyodbc
from datetime import datetime, date, timedelta
import sys
import csv
import tkinter as tk
from tkinter import messagebox



#####################################################################################################################################################

start = datetime.now().strftime('%Y-%m-%d')
end = datetime.now().strftime('%Y-%m-%d')

 
def export_Habs():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = conn.cursor()
    tabla = f'Tiempo_Limpiando_Habitacion_{num+1}'
    NumeroHab = f'Hab_{num}_Tiempo_Limpiando'
    query = f"SELECT Time_Stamp, {NumeroHab} FROM {tabla} WHERE Time_Stamp >= '{start} 00:00:00.000000' AND Time_Stamp <= '{end} 23:59:59.000000'"
    cursor.execute(query)
    rows = cursor.fetchall()

    with open("scripts\Exportaciones_Mostradas_Scada\Exportaciones_Habs.txt", mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Escribir los datos de los resultados
        for resultado in rows:
            writer.writerow(resultado)    
            
try:
    if __name__ == "__main__":
        num = int(sys.argv[1])
        server = str(sys.argv[2])
        database = str(sys.argv[3])
        print(num)
        export_Habs()
except Exception as e:
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Error", str(e)) 
    root.destroy()