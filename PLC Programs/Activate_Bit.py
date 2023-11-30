import snap7
import time
import Tools as ts
x = int(input("Which plc?\n"))
x = x + 100
y = int(input("Which Byte?\n"))
z = int(input("Which Bit?\n"))
on_off = int(input("On - 1\nOff - 0\n"))
plc = snap7.logo.Logo()
ip = f'192.168.30.{x}'
plc = ts.try_to_connect(ip, 0, 1)
plc.write(f'V{y}.{z}',on_off)
plc.disconnect()
