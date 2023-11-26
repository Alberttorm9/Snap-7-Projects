
import tkinter as tk
import configparser
import PLC_Updater
import time

config = configparser.ConfigParser()
config.read('SCADA Programs\SCADA 200\config.ini')
square_size = int(config.get('Settings', 'square_size'))
PLC_count = int(config.get('Settings', 'PLC_count'))
bytes_in_read = int(config.get('Settings', 'bytes_in_read'))
bytes_out_read = int(config.get('Settings', 'bytes_out_read'))
bytes_in_leido = 0
bytes_out_leido = 0
PLC_count = int(config.get('Settings', 'PLC_count'))
window = tk.Tk()
window.title("Programa de Cuadrados")

def create_PLC_squares():
        squares = []
        for i in range(PLC_count):
            square = tk.Frame(window, width=square_size, height=square_size, bg='blue')
            square.grid(row=i//(int(config.get('Settings', 'distributionX'))), column=i%(int(config.get('Settings', 'distributionY'))), padx=5, pady=5)
            square.bind('<Button-1>', on_square_click(i))
            squares.append(square)

def on_square_click(plc_num):
    for widget in window.winfo_children():
        widget.pack_forget()
    create_bit_squares(plc_num)

def create_bit_squares(plc_num):
        global bytes_in_leido, bytes_out_leido
        PLC_Updater.actualizador = 1
        time.sleep(1)
        lista_variables = PLC_Updater.lista_PLC
        for j in range(bytes_in_read):
            bytes_in_leido = bytes_in_leido + 1
            for i in range(7):
                if not (lista_variables[plc_num[j*bytes_in_leido[i]]]):
                    color = "red"
                else:
                    color = "green"
                square = tk.Frame(window, width=50, height=50, bg=color)
                square.grid(row=j, column=i, padx=5, pady=5)

        for j in range(bytes_out_read):
            bytes_out_leido = bytes_out_leido + 1
            for i in range(7):
                if not (lista_variables[plc_num[j*bytes_out_leido[i]]]):
                    color = "blue"
                else:
                    color = "yellow"
                square = tk.Frame(window, width=50, height=50, bg=color)
                square.grid(row=(j + int(config.get('Settings', 'bytes_in_read'))), column=i, padx=5, pady=5)  
        back_button = tk.Button(window, text='Atrás', command=on_back_button_click(back_button))
        back_button.grid(row=0, column=8, columnspan=2, pady=10)
        window.after(2000, create_bit_squares)

def on_back_button_click(back_button):
    for widget in window.winfo_children():
        widget.pack_forget()
    back_button.grid_forget()
    create_PLC_squares()


create_PLC_squares()
    
window.mainloop()