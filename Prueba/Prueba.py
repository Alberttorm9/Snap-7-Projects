
import snap7

plc = snap7.logo.Logo()
plc.connect("192.168.30.102", 0, 1)

if plc.get_connected():
    plc.write("V11.0", 1)
    a = plc.read("VW12")
    print(a)

plc.disconnect()