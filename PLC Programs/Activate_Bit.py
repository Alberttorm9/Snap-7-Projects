import snap7
import tkinter as tk

plc = snap7.logo.Logo()

def actualizar_bit():
    global after_id, PLC_Byte, PLC_Bit, plc
    estado_bit = plc.read(f'V{PLC_Byte}.{PLC_Bit}')
    print(estado_bit)  
    if estado_bit:
        bit_plc.config(bg="Green")
    else:
        bit_plc.config(bg="Red")
    if after_id == 0:
        boton_after_stop.pack(pady=10)
    else:
        boton_after_stop.config(command=volver_atras)
    after_id = root.after(1000, actualizar_bit)

def volver_atras():
    global after_id
    root.after_cancel(after_id)
    after_id = 0
    boton_after_stop.pack_forget()
    bit_plc.pack_forget()
    boton_activar.pack_forget()
    boton_desactivar.pack_forget()
    plc.disconnect()
    texto.config(text="Which PLC?")
    texto.pack()
    entrada.pack()
    boton.pack()

def plc_bit_changer():
    global PLC_Byte, PLC_Bit, plc
    bit_plc.pack(pady=10)
    boton_desactivar.pack(side=tk.RIGHT, padx=5)
    boton_activar.pack(side=tk.LEFT, padx=5)
    actualizar_bit()

def obtener_texto():
    global texto, plc, step, PLC_Byte, PLC_Bit
    if step==0:
        step += 1
        PLC_num = entrada.get()
        try:
            PLC_num = int(PLC_num)
            try:
                PLC_num = PLC_num + 100
                ip = f'192.168.30.{PLC_num}'
                plc.connect(ip, 0, 1)
                texto.config(text="Which Byte?")
            except Exception:
                try:
                    PLC_num = PLC_num + 100
                    ip = f'192.168.30.{PLC_num}'
                    plc.connect(ip, 0, 1)
                    texto.config(text="Which Byte?")
                except Exception:
                    step = 0
                    texto.config(text="Not Available, Chose other PLC")    
        except Exception:
            step = 0
            texto.config(text="Introduce a NUMBER for the PLC")
                    
    elif step == 1:
        step += 1
        PLC_Byte = entrada.get()
        try:
            PLC_Byte = int(PLC_Byte)
            texto.config(text="Which Bit?")
        except Exception:
            step = 1
            texto.config(text="Introduce a NUMBER for the Byte")
    elif step == 2:
        try:
            step = 0
            PLC_Bit = entrada.get()
            PLC_Bit = int(PLC_Bit)
            entrada.pack_forget()
            boton.pack_forget()
            texto.pack_forget()
            plc_bit_changer()
        except Exception:
            step = 2
            texto.config(text="Introduce a NUMBER for the Bit")
    entrada.delete(0, "end")

PLC_Byte = PLC_Bit = step = 0
after_id = 0
root = tk.Tk()
entrada = tk.Entry(root)
boton = tk.Button(root, text="Enter", command=obtener_texto)
texto = tk.Label(root, text="Which PLC?")
bit_plc = tk.Label(root, width=15, height=5)
boton_after_stop = tk.Button(root, text="Atrás")
boton_activar = tk.Button(root, text="Desactivar", command=lambda:plc.write(f'V{PLC_Byte}.{PLC_Bit}',0))
boton_desactivar = tk.Button(root, text="Activar", command=lambda:plc.write(f'V{PLC_Byte}.{PLC_Bit}',1))

texto.pack()

entrada.pack()

boton.pack()

root.mainloop()


 


