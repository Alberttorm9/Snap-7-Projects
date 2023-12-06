import ctypes

class Ctr571:
    def __init__(self):
        self.crt_571 = ctypes.CDLL('Pruebas_CRT\lib\CRT_571.dll')
        self.Hdle = 0

        # Definir las funciones
        self.CommOpen = self.crt_571.CommOpen
        self.CommOpen.argtypes = [ctypes.c_char_p]
        self.CommOpen.restype = ctypes.c_uint32

        self.CommOpenWithBaut = self.crt_571.CommOpenWithBaut
        self.CommOpenWithBaut.argtypes = [ctypes.c_char_p, ctypes.c_uint32]
        self.CommOpenWithBaut.restype = ctypes.c_long

        self.CommClose = self.crt_571.CommClose
        self.CommClose.argtypes = [ctypes.c_uint32]
        self.CommClose.restype = ctypes.c_int

        self.ExecuteCommand = self.crt_571.ExecuteCommand
        self.ExecuteCommand.argtypes = [ctypes.c_uint32, ctypes.c_byte, ctypes.c_byte, ctypes.c_byte, ctypes.c_uint16, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint16), ctypes.POINTER(ctypes.c_byte)]
        self.ExecuteCommand.restype = ctypes.c_int

    def Inicializar(self):
        if self.Hdle != 0:
            Addr = 0
            Cm = 0x30
            Pm = 0x30
            St0 = ctypes.c_byte(0)
            St1 = ctypes.c_byte(0)
            St2 = ctypes.c_byte(0)
            TxDataLen = 0
            RxDataLen = ctypes.c_uint16(0)
            TxData = (ctypes.c_byte * 1024)()
            RxData = (ctypes.c_byte * 1024)()
            ReType = ctypes.c_byte(0)

            i = self.ExecuteCommand(self.Hdle, Addr, Cm, Pm, TxDataLen, TxData, ctypes.byref(ReType), ctypes.byref(St0), ctypes.byref(St1), ctypes.byref(St2), ctypes.byref(RxDataLen), RxData)
            if i == 0:
                if ReType.value == 0x50:
                    print("INITIALIZE OK" + "\r\n" + "Status Code : " + chr(St0.value) + chr(St1.value) + chr(St2.value))
                else:
                    print("INITIALIZE ERROR" + "\r\n" + "Error Code:  " + chr(St1.value) + chr(St2.value))
            else:
                print("Communication Error")
        else:
            print("Comm. port is not Opened")

# Usar la clase
ctr_571 = Ctr571()
ctr_571.Hdle = ctr_571.CommOpen(b'COM1')
ctr_571.Inicializar()
