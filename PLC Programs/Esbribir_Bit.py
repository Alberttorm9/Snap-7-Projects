import snap7
import sys
ip = "192.168.30.102"
plc = snap7.logo.Logo()
plc.connect(ip, 0, 1)
plc.write("V10.0",1)
plc.disconnect()