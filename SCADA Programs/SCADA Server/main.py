import tkinter as tk
import customtkinter as ctk
import configparser
import time
from googletrans import Translator
import PLC

config = configparser.ConfigParser()
config.read('SCADA Programs\SCADA Server\config.ini')
ancho_pantalla = eval(config["Ajustes"]["ResolucionX"])
alto_pantalla = eval(config["Ajustes"]["ResolucionY"])
resolucion_pantalla = f'{ancho_pantalla}''x'f'{alto_pantalla}'

#Declaración de variables Globales y labels&buttons
Contador_Hab = 1
idioma = 0
NumHabitaciones = eval(config['Ajustes']['NumHabitaciones'])
Habitaciones = []
Precios = []

class ImageSlider(tk.Frame):
    def __init__(self, master, images):
        tk.Frame.__init__(self, master)
        self.images = images
        self.current_image = 0

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.prev_button = tk.Button(self, text="Anterior", command=self.show_previous_image)
        self.prev_button.pack(side="left")
        self.next_button = tk.Button(self, text="Siguiente", command=self.show_next_image)
        self.next_button.pack(side="right")

    def show_image(self):
        image_path = self.images[self.current_image]
        image = tk.PhotoImage(file=image_path)
        self.image_label.config(image=image)
        self.image_label.image = image  # Evita que la imagen sea eliminada por el recolector de basura

    def show_previous_image(self):
        self.current_image = (self.current_image - 1) % len(self.images)
        self.show_image()

    def show_next_image(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.show_image()

class Tipo_Habitacion:
    def __init__(self, Tipo, Precio1, Precio2, Precio3, Info):
        self.Tipo = Tipo
        self.Precios = [Precio1,Precio2,Precio3]
        self.Info = Info

for i in range(1, NumHabitaciones+1):
    Habitacion = Tipo_Habitacion(
        config[f'Habitacion{i}']['Tipo'],
        eval(config[f'Habitacion{i}']['Precio1']),
        eval(config[f'Habitacion{i}']['Precio2']),
        eval(config[f'Habitacion{i}']['Precio3']),
        config[f'Habitacion{i}']['Info']    
    )
    Habitaciones.append(Habitacion)

def ocupar_habitacion():
    PLC.read_logo_outputs()
    time.sleep(3)#Falta el mostrar habitación
    rehacer_tabla_precios()

def traducir(texto, idioma_destino):
    translator = Translator()
    traduccion = translator.translate(texto, dest=idioma_destino)
    return traduccion.text

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
    global tabla_frame, root
    tabla_frame.destroy()
    tabla_frame = tk.Frame(root, bg='lightblue')
    tabla_frame.pack()
    mostrar_pantalla_idiomas()

def mostrar_info_pagar(hab, tipo):
    ocultar_todo()
    bt_continuar = mostrar_info(hab, tipo)
    bt_continuar.place(x = (ancho_pantalla//2), y = alto_pantalla-100, anchor='ne')

def ir_a_tabla():
    ocultar_todo()
    pantalla_info.destroy()
    tabla_frame.pack()

def mostrar_agradecimiento():
    ocultar_todo()
    agradecimiento_label.pack()
    ocupar_habitacion()  

def mostrar_info(info_hab, tipo_hab):
    ocultar_todo()
    #Frame prinecipal
    pantalla_info = tk.Frame(root, bg='brown', width=ancho_pantalla, height=alto_pantalla)
    pantalla_info.place()
    #Cabecera
    cabecera_info_frame = tk.Label(pantalla_info, text=tipo_hab, font=("Arial", 40))
    cabecera_info_frame.place(x=0, y=-10, relwidth=1)
    
    #Label de información
    info_hab_label = tk.Label(pantalla_info, text=info_hab.replace('\\n', '\n'), font=("Arial", 20),bg='green')
    bt_atras = ctk.CTkButton(info_hab_label, text="Atrás", font=("Arial", 40), command=ir_a_tabla)
    bt_continuar = ctk.CTkButton(info_hab_label, text="Continuar", command=mostrar_agradecimiento, font=("Arial", 40))
    #Label de fotos
    fotos_info = tk.Label(pantalla_info, text=tipo_hab, font=("Arial", 2), bg='blue')
    ############slider = ImageSlider()
    #Pack
    pantalla_info.pack()
    #cabecera_info_frame.pack()
    info_hab_label.place(y=50, relwidth=0.5, relheight=1)
    fotos_info.place(x=root.winfo_width() // 2, y=50, relwidth=0.5, relheight=1)
    bt_atras.place(y=alto_pantalla-100)
    return bt_continuar
    
   

def crear_celda_texto(idioma):
    global Contador_Hab
    valor = f"Habitación {Contador_Hab}"
    if idioma == 'en':
        valor = traducir(valor,'en')
    elif idioma == 'pt':
        valor =traducir(valor,'pt')
    Contador_Hab += 1
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
    global alto_pantalla, ancho_pantalla
    ocultar_todo()
    inicio_frame.pack()
    canvas_inicio_frame.pack()
    canvas_inicio_frame.create_oval((ancho_pantalla//2) - 50, (alto_pantalla//2) + 50 , (ancho_pantalla//2) + 50, (alto_pantalla//2) - 50, fill="blue", tags="Ciculo_EN")
    canvas_inicio_frame.create_oval((ancho_pantalla//2) - 250, (alto_pantalla//2) + 50 , (ancho_pantalla//2) - 150, (alto_pantalla//2) - 50, fill="blue", tags="Ciculo_ES")
    canvas_inicio_frame.create_oval((ancho_pantalla//2) + 250, (alto_pantalla//2) + 50 , (ancho_pantalla//2) + 150, (alto_pantalla//2) - 50, fill="blue", tags="Ciculo_PT")
    canvas_inicio_frame.tag_bind("Ciculo_ES", "<Button-1>", lambda event: crear_tabla_precios('es'))
    canvas_inicio_frame.tag_bind("Ciculo_EN", "<Button-1>", lambda event: crear_tabla_precios('en'))
    canvas_inicio_frame.tag_bind("Ciculo_PT", "<Button-1>", lambda event: crear_tabla_precios('pt'))
    
def crear_tabla_precios(idioma):
    #Generación de cuadricula pecios
    global NumHabitaciones, Contador_Hab
    Contador_Hab = 1
    ocultar_todo()
    for i in range(NumHabitaciones):
        for j in range(1):
            celda = crear_celda_texto(idioma)
            celda.grid(row=j, column=i, padx=5, pady=5) 
        for j in range(3):
            celda = crear_celda_precio(f'{Habitaciones[i].Precios[j]}',f'{Habitaciones[i].Info}', f'{Habitaciones[i].Tipo}')
            celda.grid(row=j+1, column=i, padx=5, pady=5)
        for j in range(1):
            celda = crear_celda_info(f'{Habitaciones[i].Info}', idioma, f'{Habitaciones[i].Tipo}')
            celda.grid(row=4, column=i, padx=5, pady=5)
        if i == NumHabitaciones-1:
            for j in range(1):
                celda = crear_celda_ir_inicio(idioma)
                celda.grid(row=j, column=i+1, padx=5, pady=5)
    tabla_frame.pack()

#Uso de librería y descripción
root = tk.Tk()
root.geometry(resolucion_pantalla)
root.configure(bg='lightblue')
root.title("Programa Quiosco")

#Creación de frames
tabla_frame = tk.Frame(root, bg='lightblue')
inicio_frame = tk.Frame(root, bg='black', width=ancho_pantalla, height=alto_pantalla)
pantalla_info = tk.Frame(root, bg='brown', width=ancho_pantalla, height=alto_pantalla)
agradecimiento_frame = tk.Frame(root, bg='green')
canvas_inicio_frame = tk.Canvas(inicio_frame, width=ancho_pantalla, height=alto_pantalla)
agradecimiento_label = tk.Label(agradecimiento_frame, text="Muchas gracias", font=("Arial", 20), bg='lightblue')


#main
mostrar_pantalla_idiomas()
root.mainloop()

# def resize(e):
# 	# Grab the app width and divide by 10
# 	size = e.width / 10
# 	# Change our button text size
# 	button_1.config(font=("Helvetica", int(size)))

# 	# Mess with height
# 	height_size = e.height / 10
# 	if e.height <= 300:
# 		button_1.config(font=("Helvetica", int(height_size)))		

# 	'''
# 	if e.height <= 300 and e.height > 200:
# 		button_1.config(font=("Helvetica", 30))
# 	elif e.height < 200 and e.height > 100:
# 		button_1.config(font=("Helvetica", 20))		 		
# 	elif e.height < 100:
# 		button_1.config(font=("Helvetica", 10))		 		
# 	'''

# # Bind the app 
# root.bind('<Configure>', resize)