import snap7
import time
ip = "192.168.30.104"
plc = snap7.logo.Logo()
plc.connect(ip, 0, 1)
plc.write("V10.1",1)
time.sleep(0.5)
plc.write("V10.1",0)

plc.disconnect()