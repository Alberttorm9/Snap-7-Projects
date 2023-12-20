import tkinter as tk
import customtkinter as ctk
import configparser
import main_config
import time

config = configparser.ConfigParser()
config.read('SCADA Programs\SCADA Server\Caracteristicas_Habitaciones.ini')
resolucion_pantalla = config["Ajustes"]["ResolucionX"]+"x"+config["Ajustes"]["ResolucionY"]

#Declaración de variables Globales y labels&buttons
NumHabitaciones = eval(config['Ajustes']['NumHabitaciones'])
Habitaciones = []


for i in range(1, NumHabitaciones+1):
    Habitacion = (
        config[f'Habitacion{i}']['Tipo'],
        eval(config[f'Habitacion{i}']['Precio1']),
        eval(config[f'Habitacion{i}']['Precio2']),
        eval(config[f'Habitacion{i}']['Precio3']),
        config[f'Habitacion{i}']['Info']    
    )
    Habitaciones.append(Habitacion)
    
root = tk.Tk()
root.geometry(resolucion_pantalla)
root.overrideredirect(1)
root.title("Quiosco")
root.mainloop()