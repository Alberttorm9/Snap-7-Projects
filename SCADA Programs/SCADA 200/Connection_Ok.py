import snap7

def try_to_connect(ip, rack, slot):
    plc = snap7.logo.Logo()
    try:
     plc.connect(ip, rack, slot)
     return(True)
    except Exception:
        try:
            plc.connect(ip, rack, slot)
            return(True)    
        except Exception:
            return (False)
        