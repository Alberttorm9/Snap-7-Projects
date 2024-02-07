import pyodbc
from datetime import datetime, date
import csv
import sys

#####################################################################################################################################################

start = date.today().replace(day=1).strftime('%Y-%m-%d')
end = datetime.now().strftime('%Y-%m-%d')

 
def export_Habs():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
    cursor = conn.cursor()
    tabla = f'Tiempo_Limpiando_Habitacion_{num+1}'
    NumeroHab = f'Hab_{num}_Tiempo_Limpiando'
    query = f"SELECT Time_Stamp, {NumeroHab} FROM {tabla} WHERE Time_Stamp >= '{start} 00:00:00.000000' AND Time_Stamp <= '{end} 23:59:59.000000'"
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        with open("scripts\Exportaciones_Mostradas_Scada\Exportaciones_Habs.txt", mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Escribir los datos de los resultados
            for resultado in rows:
                writer.writerow(resultado)    
    except Exception as e:
        if "42S02" in str(e):
            with open("scripts\Exportaciones_Mostradas_Scada\Exportaciones_Habs.txt", mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Escribir los datos de los resultados
                writer.writerow(["NO DATA" , "EXPORT ERROR"])        

if __name__ == "__main__":
    num = int(sys.argv[1])
    server = str(sys.argv[2])
    database = str(sys.argv[3])
    # num = 7
    # server = "LAPTOP-3UQV2BFJ\SQLEXPRESS"
    # database = "Motel_Panama"
    print(num)
    export_Habs()

        