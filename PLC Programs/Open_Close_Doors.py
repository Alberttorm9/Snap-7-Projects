import snap7
import time
import Tools as ts
act = 3
plc = snap7.logo.Logo()
print("Start from PLC X And End PLC Y")
plcx = int(input(f'Enter Start PLC: '))
plcx = plcx + 100
plcy = int(input(f'Enter End PLC: '))
plcy = plcy +101
for i in range(int(plcy - plcx)):
    ip = f'192.168.30.{plcx + i}'
    if act == 3:
        act = int(input("\n\nOpen or close all?\nYes - 2\nGo step x step - 1\nNo - 0\n\n"))
    if act == 1:
        plc = ts.try_to_connect(ip, 0, 1)
        if plc.read("V12.2"):
            yes_no = input(f'\nDoor {plcx + i} Closed, Do you want to open it?\n\nYes or No\n')
            if yes_no == ("YES" or "Yes" or "yes"):
                plc.write("V10.1",1)
                time.sleep(0.5)
                plc.write("V10.1",0)
                plc.disconnect()
        elif plc.read("V12.3"):
            yes_no = input(f'\nDoor {plcx + i} Opened, Do you want to close it?\nYes or No\n')
            if yes_no == ("YES" or "Yes" or "yes"):
                plc.write("V10.1",1)
                time.sleep(0.5)
                plc.write("V10.1",0)
                plc.disconnect()
        else:
            print(f'\nError in plc {plcx + i} Not opened and not closed')
            yes_no = input(f'\nDoor {plcx + i} in the middle, Do you want to move it?\nYes or No\n')
            if yes_no == ("YES" or "Yes" or "yes"):
                plc.write("V10.1",1)
                time.sleep(0.5)
                plc.write("V10.1",0)
                plc.disconnect()
    elif act == 2:
        ts.try_to_connect(ip, 0, 1)
        plc.write("V10.1",1)
        time.sleep(0.5)
        plc.write("V10.1",0)
        plc.disconnect()