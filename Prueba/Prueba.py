import snap7
import time
import Tools as ts
import tkinter as tk

plc = snap7.logo.Logo()

# Crear la ventana
root = tk.Tk()
PLC_Byte = PLC_Bit = 1
# Crear un frame para contener los elementos
frame = tk.Frame(root)
frame.pack()

# Crear un cuadrado de color verde en el centro del frame
cuadrado = tk.Label(frame, width=10, height=5, bg="green")
cuadrado.pack(pady=10)
ip = f'192.168.30.101'
plc = ts.try_to_connect(ip, 0, 1)
plc.write(f'V{PLC_Byte}.{PLC_Bit}',1)
# Crear botones para cambiar el color del cuadrado
boton_rojo = tk.Button(root, text="Activar", command=lambda:plc.write(f'V{PLC_Byte}.{PLC_Bit}',1))
boton_rojo.pack(side=tk.RIGHT, padx=5)

# Mostrar la ventana
root.mainloop()