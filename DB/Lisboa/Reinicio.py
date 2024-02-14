import snap7
import sys
plc = snap7.logo.Logo()
num=0
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num = int(sys.argv[1])
        
    ip = f'192.168.30.{num + 101}'
    plc.connect(ip, 0, 1)
    for i in range(40):
        plc.write(f'VW{i}', 0)
    plc.write("V0.1",1)
    plc.write("VW14", 1)
    plc.write("V0.1",0)
    plc.disconnect()
