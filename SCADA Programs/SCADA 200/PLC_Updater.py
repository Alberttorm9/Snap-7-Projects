import snap7
import configparser
config = configparser.ConfigParser()
config.read('Snap-7-Projects\SCADA Programs\SCADA 200\config.ini')
PLC_count = int(config.get('Settings', 'PLC_count'))
bytes_in_read = int(config.get('Settings', 'bytes_in_read'))
bytes_out_read = int(config.get('Settings', 'bytes_out_read'))
lista_in = []
lista_out = []
lista_in_out = []
lista_PLC = []
plc = snap7.logo.Logo()

#while actualizador:
def decimal_a_binario(decimal):
    binario = []
    while decimal > 0:
        binario.insert(0, decimal % 2)
        decimal = decimal // 2
    binario.reverse()
    if len(binario) < 8:
        ceros_faltantes = 8 - len(binario)
        binario.extend([0] * ceros_faltantes)
    return binario
def actualizador(plc_num):
    lista_in.clear()
    lista_out.clear()
    lista_in_out.clear()
    while not (plc.get_connected()):
        try:
            plc.connect(f'192.168.30.{plc_num+101}', 0, 1)
        except Exception:
            plc.connect(f'192.168.30.{plc_num+101}', 0, 1)
    for j in range(bytes_in_read):
            lectura_variable = plc.read(f'V102{j+4}')
            lista_in.append(decimal_a_binario(lectura_variable))
    for j in range(bytes_out_read):
            lectura_variable = plc.read(f'V106{j+4}')
            lista_out.append(decimal_a_binario(lectura_variable))

    lista_in_out.append(lista_in)
    lista_in_out.append(lista_out)
    print(lista_in_out)
    plc.disconnect()
    return lista_in_out

a = actualizador(0)       