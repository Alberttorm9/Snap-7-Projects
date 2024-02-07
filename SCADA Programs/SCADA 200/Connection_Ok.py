import snap7

def try_to_connect(ip, rack, slot):
    plc = snap7.logo.Logo()
    try:
     plc.connect(ip, rack, slot)
     plc.set_param(snap7.types.PingTimeout, 200)
     return(True)
    except Exception:
        try:
            plc.connect(ip, rack, slot)
            plc.set_param(snap7.types.PingTimeout, 200)
            return(True)    
        except Exception:
            return (False)
        