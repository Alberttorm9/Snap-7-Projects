import snap7
import time 

inicio = time.time()
def asci_conversor(valor):
    bin_str = bin(valor)[2:]
    bit_table = [f'(I{i+1} = {int(bit)})' for i, bit in enumerate(bin_str[::-1])]
    bit_table = str(bit_table)
    bit_table = bit_table.replace("'","")
    return bit_table

def conect_to_logo(ip):
    # Crear un cliente
    PLC = snap7.logo.Logo()
    # Conectar al PLC
    PLC.connect(ip, 0, 1)
    return PLC

def reed_di(PLC):
    # Leer las salidas digitales
    output = PLC.read("V1024")
    return output


if 0==1:
    for i in range(40):
        ip = f'192.168.30.{i+101}'
        PLC = conect_to_logo(ip)
        PLC1 = conect_to_logo(ip)
        result =reed_di(PLC)
        result = asci_conversor(result)
        result =f'PLC {i+1}' + result
        print(result)   
            
    result =reed_di(PLC)
    tabla_resultados = asci_conversor(result)
    result =reed_di(PLC1)
    tabla_resultados = tabla_resultados + "\n" + asci_conversor(result)

fin = time.time()
tiempo_transcurrido = fin - inicio
print(f"La línea de código tardó {tiempo_transcurrido} segundos en ejecutarse.")