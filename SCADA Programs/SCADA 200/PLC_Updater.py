import snap7
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
PLC_count = int(config.get('Settings', 'PLC_count'))
bytes_in_read = int(config.get('Settings', 'bytes_in_read'))
bytes_out_read = int(config.get('Settings', 'bytes_out_read'))
lista_in = []
lista_out = []
lista_in_out = []
lista_PLC = []
plc = snap7.logo.Logo()
plc.set_param(snap7.types.PingTimeout, 200)
simulador = 0
cambiar_valores_simulados = 0

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
    global cambiar_valores_simulados
    lista_in.clear()
    lista_out.clear()
    lista_in_out.clear()

    if not simulador:
        while not (plc.get_connected()):
            try:
                plc.connect(f'192.168.30.{plc_num+101}', 0, 1)
            except Exception:
                try:
                    plc.connect(f'192.168.30.{plc_num+101}', 0, 1)
                except Exception:
                    return 0
        for j in range(bytes_in_read):
                lectura_variable = plc.read(f'V102{j+4}')
                lista_in.append(decimal_a_binario(lectura_variable))
        for j in range(bytes_out_read):
                lectura_variable = plc.read(f'V106{j+4}')
                lista_out.append(decimal_a_binario(lectura_variable))
        plc.disconnect()
    else:
        cambiar_valores_simulados += 1
        if cambiar_valores_simulados < 5:
            lectura_variable = 15
            lista_in.append(decimal_a_binario(lectura_variable))
            lectura_variable = 21
            lista_in.append(decimal_a_binario(lectura_variable))
            lectura_variable = 86
            lista_out.append(decimal_a_binario(lectura_variable))
            lectura_variable = 25
            lista_out.append(decimal_a_binario(lectura_variable))
        elif (cambiar_valores_simulados > 4) and (cambiar_valores_simulados < 10):
            lectura_variable = 86
            lista_in.append(decimal_a_binario(lectura_variable))
            lectura_variable = 24
            lista_in.append(decimal_a_binario(lectura_variable))
            lectura_variable = 124
            lista_out.append(decimal_a_binario(lectura_variable))
            lectura_variable = 254
            lista_out.append(decimal_a_binario(lectura_variable))
        else:
            lectura_variable = 233
            lista_in.append(decimal_a_binario(lectura_variable))
            lectura_variable = 2
            lista_in.append(decimal_a_binario(lectura_variable))
            lectura_variable = 168
            lista_out.append(decimal_a_binario(lectura_variable))
            lectura_variable = 101
            lista_out.append(decimal_a_binario(lectura_variable))


    lista_in_out.append(lista_in)
    lista_in_out.append(lista_out)
    print(lista_in_out)
    print(f'Estas leyendo el plc 192.168.30.{plc_num+101}')
    return lista_in_out
