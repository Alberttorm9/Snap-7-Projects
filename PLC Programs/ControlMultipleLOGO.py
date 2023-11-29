import snap7
import string
import time

#V10.0 = Lector De Tarjetas ---------- V12.0 = Luz RGB verde
#V10.1 = Pulsador Portal ---------- V12.1 = Abrir/Cerrar Portal
#V10.2 = Portal Cerrado ---------- V12.2 = Luz RGB Azul
#V10.3 = Portal Abierto ---------- V12.3 = Luz RGB Roja
#V10.4 = Forzar Luz Numero ---------- V12.4 = Luz Numero
#V10.5 = Detección coche ---------- V12.5 = Otra luz coche
#V10.6 = Forzar Alimentación (Negado) ---------- V12.6 = Alimentación
# ---------- V12.7 = Fallo alimentacion garaje

pulsador_portal = "V10.1"
portal_cerrado = "V12.2"
portal_abierto = "V12.3"

cantidad_de_habitaciones = 40
numero_fallidos = 0
plc_a_leer = 0
portales_ya_cerrados = []
portales_ya_abiertos = []
portales_ni_cerrados_ni_abiertos = []
portales_fallidos = []

# Solicitar al usuario que ingrese un número
accion = int(input("\nQue quiere hacer?\nAbirir Portales - 1\nCerrar Portales - 2\nApagar Variables - 3\nLeer Variables - 4\n"))
if accion == 1:
    accion = int(input("\nSeguro?\nSi\nNo\n\n"))
    inicio_tiempo = time.time()
    if accion==(1):
        print("\n")
        for i in range(cantidad_de_habitaciones):
            plc = snap7.logo.Logo()
            try:
                plc.connect(f'192.168.30.{i+101}', 0, 1)
                if plc.read(f'{portal_cerrado}'):
                    plc.write(f'{pulsador_portal}', 1)
                    time.sleep(0.5)
                    plc.write(f'{pulsador_portal}', 0)
                    print(f"PLC {i+101} Abriendo")
                elif plc.read(f'{portal_abierto}'):
                    portales_ya_abiertos.append(i+101)
                else:
                    portales_ni_cerrados_ni_abiertos.append(i+101)
                plc.disconnect()
            except Exception as err:
                print(f"PLC {i+101} Error")
                portales_fallidos.append(i+101)

    print(f"\n\nFallaron: {len(portales_fallidos)}")
    print(f'Los fallidos son: {portales_fallidos}')
    print(f"Ya abiertos: {len(portales_ya_abiertos)}")
    print(f'Los ya abiertos son: {portales_ya_abiertos}')
    print(f"Portales ni abiertos ni cerrados: {len(portales_ni_cerrados_ni_abiertos)}")
    print(f'Los ni abiertos ni cerrados son: {portales_ni_cerrados_ni_abiertos}')
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(f"\nEl tiempo de ejecución fue de {tiempo_ejecucion} segundos.")

elif accion == 2:
    accion = input("\nSeguro?\nSi\nNo\n\n")
    inicio_tiempo = time.time()
    print("\n")
    for i in range(cantidad_de_habitaciones):
        plc = snap7.logo.Logo()
        try:
            plc.connect(f'192.168.30.{i+101}', 0, 1)
            if plc.read(f'{portal_abierto}'):
                plc.write(f'{pulsador_portal}', 1)
                time.sleep(0.5)
                plc.write(f'{pulsador_portal}', 0)
                print(f"PLC {i+101} Cerrando")
            elif plc.read(f'{portal_cerrado}'):
                portales_ya_cerrados.append(i+101)
            else:
                portales_ni_cerrados_ni_abiertos.append(i+101)
            plc.disconnect()
        except Exception as err:
            print(f"PLC {i+101} Error")
            portales_fallidos.append(i+101)

    print(f"\n\nFallaron: {len(portales_fallidos)}")
    print(f'Los fallidos son: {portales_fallidos}')
    print(f"Ya cerrados: {len(portales_ya_cerrados)}")
    print(f'Los ya cerrados son: {portales_ya_cerrados}')
    print(f"Portales ni abiertos ni cerrados: {len(portales_ni_cerrados_ni_abiertos)}")
    print(f'Los ni abiertos ni cerrados son: {portales_ni_cerrados_ni_abiertos}')
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(f"\nEl tiempo de ejecución fue de {tiempo_ejecucion} segundos.")

elif accion == 3:
    inicio_tiempo = time.time()
    for i in range(10):
        plc = snap7.logo.Logo()
        try:
            plc.connect(f'192.168.30.{i+101}', 0, 1)
            plc.write("V10", 0)
            plc.disconnect()
            print(f'Variables del PLC {i+101} desactivadas')
        except Exception:
            print(f"Error de conexión al PLC {i+101}")
            numero_fallidos += 1
    if numero_fallidos == 0:
        print(f"Todas las variables apagadas")
    else:
        print(f'\n\nHan fallado {numero_fallidos} PLCs\n\n')
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(f"El tiempo de ejecución fue de {tiempo_ejecucion} segundos.")

elif accion == 4:
    while (plc_a_leer < 1) or (plc_a_leer > cantidad_de_habitaciones):
        plc_a_leer = int(input(f'Que logo quieres leer:\nSelecciona de 1 a {cantidad_de_habitaciones}\n'))
        if (plc_a_leer < 1) or (plc_a_leer > cantidad_de_habitaciones):
            print("Introduzca un valor en rango")
            time.sleep(2)
    inicio_tiempo = time.time()
    plc = snap7.logo.Logo()
    plc_a_leer = plc_a_leer + 100
    try:
        print(f'Leyendo el 192.168.30.{plc_a_leer}')
        plc.connect(f'192.168.30.{plc_a_leer}', 0, 1)
        for j in range(8):
            lectura_variable = plc.read(f'V12.{j}')
            if lectura_variable == 1:
                lectura_variable = True
            else:
                lectura_variable = False
            print(f'La variable V12.{j} es {lectura_variable}')
        plc.disconnect()
        print("Variables Leidas")
    except Exception as err:
        print("No se pudo conectar al PLC")
    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print(f"El tiempo de ejecución fue de {tiempo_ejecucion} segundos.")
    time.sleep(3)
else:
    print("Opcion no disponible")