import tkinter as tk
import customtkinter as ctk
import Tools
import PLC
import time

#Declaración de variables Globales y Configs
Habitaciones = Tools.info_habs()
NumHabitaciones= Tools.NumHabitaciones()
ResolucionX = Tools.resolucionX()
ResolucionY = Tools.resolucionY()
#Declaración del root
root = tk.Tk()
root.geometry(Tools.resolucion())
root.overrideredirect(1)
root.title("Quiosco")




def crear_celda_precio(precio,info, tipo):
    celda = tk.Label(tabla_frame, text=precio + "€", font=("Arial", 12), height=2, width=10, bg='lightblue')
    celda.bind("<Button-1>", lambda event, : mostrar_info_pagar(info, tipo))
    return celda

def crear_tabla_precios(idioma):
    #Generación de cuadricula pecios
    ocultar_todo()
    for i in range(NumHabitaciones):
        for j in range(1):
            celda = crear_celda_texto(idioma, i)
            celda.grid(row=j, column=i, padx=5, pady=5) 
        for j in range(3):
            celda = crear_celda_precio(f'{Habitaciones[i][j+1]}',f'{Habitaciones[i][4]}', f'{Habitaciones[i][0]}')
            celda.grid(row=j+1, column=i, padx=5, pady=5)
        for j in range(1):
            celda = crear_celda_info(f'{Habitaciones[i][4]}', idioma, f'{Habitaciones[i][0]}')
            celda.grid(row=4, column=i, padx=5, pady=5)
        if i == NumHabitaciones-1:
            for j in range(1):
                celda = crear_celda_ir_inicio(idioma)
                celda.grid(row=j, column=i+1, padx=5, pady=5)
    tabla_frame.pack()



def ocupar_habitacion():
    PLC.read_logo_outputs()
    time.sleep(3)#Falta el mostrar habitación
    rehacer_tabla_precios()

def traducir(texto, idioma_destino):
    a = 1###################################################################################################

def ocultar_todo():
    for widget in root.winfo_children():
        widget.pack_forget()
    canvas_inicio_frame.pack_forget()

def crear_celda_ir_inicio(idioma):
    valor = "Atras"
    if idioma == 'en':
        valor = traducir(valor,'en')
    elif idioma == 'pt':
        valor =traducir(valor,'pt')
    celda = tk.Label(tabla_frame, text=valor, font=("Arial", 12), wraplength=150, bg='lightblue')
    celda.bind("<Button-1>", lambda event, : rehacer_tabla_precios())
    return celda  

def rehacer_tabla_precios():
    tabla_frame.destroy()
    mostrar_pantalla_idiomas()

def mostrar_info_pagar(hab, tipo):
    ocultar_todo()
    bt_continuar = mostrar_info(hab, tipo)
    bt_continuar.place(x = (ResolucionX//2), y = ResolucionY-100, anchor='ne')

def ir_a_tabla():
    ocultar_todo()
    pantalla_info_root.destroy()

def mostrar_agradecimiento():
    ocultar_todo()
    agradecimiento_label.pack()
    ocupar_habitacion()  

def mostrar_info(info_hab, tipo_hab):
    ocultar_todo()
    pantalla_info_top = tk.Frame(pantalla_info_root, bg='yellow')
    pantalla_info_mid = tk.Frame(pantalla_info_root, bg='brown')
    pantalla_info_foot = tk.Frame(pantalla_info_root, bg='brown')

    #Frame prinecipal
    pantalla_info_root.grid()
    pantalla_info_top.grid()
    pantalla_info_mid.grid()
    pantalla_info_foot.grid()
    #Cabecera
    texto_tipo_habitacion = tk.Label(pantalla_info_top, bg='yellow', text=tipo_hab, font=("Arial", 40))
    texto_tipo_habitacion.grid(row=0,column=0)
    
    #Label de información
    info_hab_label = tk.Label(pantalla_info_mid, text=info_hab.replace('\\n', '\n'), font=("Arial", 20),bg='green')
    info_hab_label.grid(row=0,column=0)
    #Label de fotos
    fotos_info = tk.Label(pantalla_info_mid, text=tipo_hab, font=("Arial", 2), bg='blue')
    fotos_info.grid(row=0, column=1)
    ############slider = ImageSlider()
    bt_atras = ctk.CTkButton(pantalla_info_foot, text="Atrás", font=("Arial", 40), command=ir_a_tabla)
    bt_continuar = ctk.CTkButton(pantalla_info_foot, text="Continuar", command=mostrar_agradecimiento, font=("Arial", 40))


    bt_atras.grid(row=0)
    bt_continuar.grid(row=0)##############################################################################################FALTA QUE ESTÉ SOLO SEPARADO POR LA IZQUIERDA
    return bt_continuar
    
   

def crear_celda_texto(idioma, Contador_Hab):
    valor = f"Habitación {Contador_Hab + 1}"
    celda = tk.Label(tabla_frame, text=str(valor), font=("Arial", 12), height=2, width=10, bg='lightblue')
    return celda

def crear_celda_precio(precio,info, tipo):
    celda = tk.Label(tabla_frame, text=precio + "€", font=("Arial", 12), height=2, width=10, bg='lightblue')
    celda.bind("<Button-1>", lambda event, : mostrar_info_pagar(info, tipo))
    return celda

def crear_celda_info(hab, idioma, tipo):
    valor = "+información"
    if idioma == 'en':
        valor = traducir(valor,'en')
    elif idioma == 'pt':
        valor =traducir(valor,'pt')
    celda = tk.Label(tabla_frame, text=str(valor), font=("Arial", 12), wraplength=150, bg='lightblue')
    celda.bind("<Button-1>", lambda event, v=valor: mostrar_info(hab, tipo))
    return celda

def mostrar_pantalla_idiomas():
    ocultar_todo()
    canvas_inicio_frame.pack()
    canvas_inicio_frame.create_oval((ResolucionX//2) - 50, (ResolucionY//2) + 50 , (ResolucionX//2) + 50, (ResolucionY//2) - 50, fill="blue", tags="Ciculo_EN")
    canvas_inicio_frame.tag_bind("Ciculo_EN", "<Button-1>",lambda event: crear_tabla_precios('es'))
    canvas_inicio_frame.create_oval((ResolucionX//2) - 250, (ResolucionY//2) + 50 , (ResolucionX//2) - 150, (ResolucionY//2) - 50, fill="blue", tags="Ciculo_ES")
    canvas_inicio_frame.tag_bind("Ciculo_ES", "<Button-1>",lambda event: crear_tabla_precios('en'))
    canvas_inicio_frame.create_oval((ResolucionX//2) + 250, (ResolucionY//2) + 50 , (ResolucionX//2) + 150, (ResolucionY//2) - 50, fill="blue", tags="Ciculo_PT")
    canvas_inicio_frame.tag_bind("Ciculo_PT", "<Button-1>",lambda event: crear_tabla_precios('pt'))



#Creación de frames
tabla_frame = tk.Frame(root, bg='lightblue', padx= 400, pady=400)
canvas_inicio_frame = tk.Canvas(root, width=ResolucionX, height=ResolucionY)
pantalla_info_root = tk.Frame(root, bg='yellow')
pantalla_info_top = tk.Frame(pantalla_info_root, bg='yellow')
pantalla_info_mid = tk.Frame(pantalla_info_root, bg='brown', width=ResolucionX)
pantalla_info_foot = tk.Frame(pantalla_info_root, bg='brown')

agradecimiento_frame = tk.Frame(root, bg='green')
agradecimiento_label = tk.Label(agradecimiento_frame, text="Muchas gracias", font=("Arial", 20), bg='lightblue')

mostrar_pantalla_idiomas()
root.mainloop()