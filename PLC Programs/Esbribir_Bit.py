import snap7
import time
import Tools as ts
act = 3
plc = snap7.logo.Logo()

for i in range(4):
    ip = f'192.168.30.{i+101}'
    if act == 3:
        act = int(input("Open or close all?\nYes - 2\nGo step x step - 1\nNo - 0\n\n"))
    if act == 1:
        plc = ts.try_to_connect(ip, 0, 1)
        if plc.read("V12.2"):
            si_no = input(f'\nPortal {ip} Cerrado, Desea Abrir?\n\nSi - 1\nNo - 0\n')
            if si_no:
                plc.write("V10.1",1)
                time.sleep(0.5)
                plc.write("V10.1",0)
        elif plc.read("V12.3"):
            si_no = input(f'\nPortal {ip} Abierto, Desea Cerrar?\nSi - 1\nNo - 0\n')
            if si_no:
                plc.write("V10.1",1)
                time.sleep(0.5)
                plc.write("V10.1",0)
        else:
            print(f'Error en plc {ip}')
        plc.disconnect()
    elif act == 2:
        ts.try_to_connect(ip, 0, 1)
        plc.write("V10.1",1)
        time.sleep(0.5)
        plc.write("V10.1",0)
        plc.disconnect()