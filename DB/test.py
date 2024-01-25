import pyodbc
import datetime

# Establecer la conexión con la base de datos
server = 'LAPTOP-3UQV2BFJ\\SQLEXPRESS'
database = 'Motel_Panamá'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()

# Obtener la fecha de hoy en formato adecuado para SQL Server
hoy = datetime.date.today().strftime('%Y-%m-%d')

# Consulta para obtener los datos de hoy en la tabla "Tiempo_Limpiando_Habitacion_1"
query = "SELECT * FROM Tiempo_Limpiando_Habitacion_1 WHERE Time_Stamp = '" + hoy + "'"
cursor.execute(query)

# Recuperar los datos y imprimirlos
for row in cursor:
    print(row)

# Cerrar la conexión
conn.close()