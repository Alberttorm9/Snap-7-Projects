import snap7
import time
import Tools as ts
x = int(input("Que plc?\n"))
x = x + 100
plc = snap7.logo.Logo()
ip = f'192.168.30.{x}'
plc = ts.try_to_connect(ip, 0, 1)
plc.write("V0.0",1)
time.sleep(0.5)
plc.write("V0.0",0)
plc.disconnect()
