import snap7

# Create a client object
plc = snap7.client.Client()

# Connect to the PLC
plc.connect('192.168.30.131', 0, 1)

plc.set_param(snap7.types.SendTimeout,100)
recv_timeout = plc.get_param(snap7.types.SendTimeout)
print(recv_timeout)
plc.disconnect()
for i in range(10):
    try:
        plc.connect('192.168.30.131', 0, 1)
    except Exception as e:
        print(e)
        i=i+1
