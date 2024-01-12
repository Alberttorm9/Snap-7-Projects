import snap7
from snap7.util import *

# Dirección IP del PLC simulado
plc_ip = "192.168.30.101"

# Crear una instancia del cliente
plc = snap7.client.Client()

# Establecer la conexión con el PLC simulado
plc.connect(plc_ip, 0, 1)

# Leer un valor de un área de memoria del PLC (por ejemplo, DB1, real)
data = plc.read_area(Areas.PE, 1, 0, 4)  # Lee un valor real de 4 bytes desde el área DB1, offset 0

# Convertir los datos a un número real
real_value = snap7.util.get_real(data, 0)

# Imprimir el valor leído
print(f"El valor real leído desde el PLC es: {real_value}")

# Cerrar la conexión con el PLC
plc.disconnect()