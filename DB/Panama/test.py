import snap7

plc = snap7.logo.Logo()
plc.connect("192.168.30.110", 0, 1)
plc.write("V80.0", 0)