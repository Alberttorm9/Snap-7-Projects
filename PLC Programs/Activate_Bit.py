import snap7
import tkinter as tk

plc = snap7.logo.Logo()

def actualizar_bit():
    global after_id, PLC_Byte, PLC_Bit, plc
    estado_bit = plc.read(f'V{PLC_Byte}.{PLC_Bit}')  
    if estado_bit:
        bit_plc.config(bg="Green")
    else:
        bit_plc.config(bg="Red")

    after_id = root.after(1000, actualizar_bit)
    
def plc_bit_changer():
    global PLC_Byte, PLC_Bit, plc
    bit_plc.pack(pady=10)
    boton_rojo = tk.Button(root, text="Activar", command=lambda:plc.write(f'V{PLC_Byte}.{PLC_Bit}',1))
    boton_rojo.pack(side=tk.RIGHT, padx=5)
    boton_verde = tk.Button(root, text="Desactivar", command=lambda:plc.write(f'V{PLC_Byte}.{PLC_Bit}',0))
    boton_verde.pack(side=tk.LEFT, padx=5)
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
        texto.config(text="Which Bit?")
    elif step == 2:
        step = 0
        PLC_Bit = entrada.get()
        entrada.pack_forget()
        boton.pack_forget()
        texto.pack_forget()
        plc_bit_changer()
    entrada.delete(0, "end")

PLC_Byte = PLC_Bit = step = 0
after_id = 0
root = tk.Tk()
entrada = tk.Entry(root)
boton = tk.Button(root, text="Enter", command=obtener_texto)
texto = tk.Label(root, text="Which PLC?")
bit_plc = tk.Label(root, width=15, height=5)

texto.pack()

entrada.pack()

boton.pack()

root.mainloop()


 


