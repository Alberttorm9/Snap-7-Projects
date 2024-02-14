import snap7
import pyodbc

server="LAPTOP-3UQV2BFJ\SQLEXPRESS"
database="Motel_Panama"
table="Ocupaciones"
conn = pyodbc.connect(f'DRIVER={"SQL Server"};SERVER={server};DATABASE={database};Trusted_Connection=yes')
cursor = conn.cursor()


def modify_database(table, valor, i):
    query = f"UPDATE {table} SET Numero_Ocupaciones = ? WHERE Habitacion = ?"
    cursor.execute(query, valor, i)
    conn.commit()

def create_table_with_values(server, database, table, data):
    # Crear la conexión
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')

    # Crear un cursor
    cursor = conn.cursor()

    # Verificar si la tabla existe
    cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = N'{table}'")
    if not cursor.fetchone():
        # Si la tabla no existe, crearla
        cursor.execute(f"CREATE TABLE {table} (Habitacion CHAR(13), Numero_Ocupaciones INT)")

    # Insertar los valores
    for row in data:
        cursor.execute(f"INSERT INTO {table} VALUES (?, ?)", row)

    # Confirmar los cambios
    conn.commit()

data = [(f"Habitación {i}", 0) for i in range(1, 37)]

cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Ocupaciones'")
if not cursor.fetchone():
    create_table_with_values(server,database,table, data)

plc= snap7.logo.Logo()
while True:
    valor = 0
    while valor == 0:
        for i in range(36):
            try:
                plc.connect(f'192.168.30.{101+i}',0,1)
                valor = plc.read("VW18")
                modify_database(table, valor, f'Habitación {i+1}')
                plc.disconnect()
            except Exception as e:
                print(e)
