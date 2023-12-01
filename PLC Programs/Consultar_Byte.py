import snap7
import sys
ip = "192.168.30.103"
byte = "V1064"
plc = snap7.logo.Logo()
plc.connect(ip, 0, 1)
for j in range(8):
        try:
            lectura_variable = plc.read(f'{byte}.{j}')
            if lectura_variable == 1:
                lectura_variable = True
                print(f'La variable {byte}.{j} es {lectura_variable}')
                en_on = en_on + 1
        except Exception:
            sys.exit()
plc.disconnect()
print(f'Variables En On: {en_on}')