import snap7
import sys

byte = "V1064"
plc = snap7.logo.Logo()

for i in range(40):
    try: 
        ip = f'192.168.30.{i+101}'
        plc.connect(ip, 0, 1)
        try:
            if plc.read("12.2"):
                print(f'PLC {i+101} Cerrado') 
            elif plc.read("12.3"):
                print(f'PLC {i+101} Abierto') 
            else:
                print(f'PLC {i+101} Ni Abierto Ni Cerrado')
            plc.disconnect()
        except Exception as a:
            print(a)
    except Exception:
         print("Error")
