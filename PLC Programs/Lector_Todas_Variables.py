import snap7
import sys

plc = snap7.logo.Logo()

print(f'Leyendo el 192.168.30.104')
plc.connect(f'192.168.30.104', 0, 1)
en_on = 0
for i in range(2000):
    for j in range(8):
            try:
                lectura_variable = plc.read(f'V{i}.{j}')
                if lectura_variable == 1:
                    lectura_variable = True
                    print(f'La variable V{i}.{j} es {lectura_variable}')
                    en_on = en_on + 1
            except Exception:
                print(f'V{i}.{j}') 
                sys.exit()
plc.disconnect()
print(f'Variables En On: {en_on}')