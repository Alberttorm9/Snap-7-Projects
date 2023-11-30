
import tkinter as tk
import configparser
import PLC_Updater
import time

def create_bit_squares(plc_num):
        lista_variables = PLC_Updater.actualizador(plc_num)
        print(lista_variables)
        for j in range(bytes_in_read):
            for k in range(7):
                if not (lista_variables[0][j][k]):

                    color = "red"
                else:
                    color = "green"
                square = tk.Frame(Bit_frame, width=50, height=50, bg=color)
                square.grid(row=j, column=k, padx=5, pady=5)
                Bit_Squares.append(square)

        for j in range(bytes_out_read):
            for k in range(7):
                if not (lista_variables[1][j][k]):
                    color = "blue"
                else:
                    color = "yellow"
                square = tk.Frame(Bit_frame, width=50, height=50, bg=color)
                square.grid(row=(j + int(config.get('Settings', 'bytes_in_read'))), column=k, padx=5, pady=5)  
                Bit_Squares.append(square)
        
        back_button = tk.Button(Bit_frame, text='Atrás', command=on_back_button_click)
        back_button.grid(row=0, column=8, columnspan=2, pady=10)
        #window.after(1000, actualizar(plc_num,Bit_Squares))

def actualizar(plc_num, Bit_Squares):
    lista_variables = PLC_Updater.actualizador(plc_num)
    for j in range(bytes_in_read):
        for k in range(7):
            if not (lista_variables[0][j][k]):
                Bit_Squares[(int(j*7))].config(bg='black')
            else:
                Bit_Squares[(int(j*7))].config(bg='brown')

    for j in range(bytes_out_read):
        for k in range(7):
            if not (lista_variables[1][j][k]):
                Bit_Squares[(int(j*7))].config(bg='black')
            else:
                Bit_Squares[(int(j*7))].config(bg='brown')

        

def create_PLC_squares():
        PLC_frame.grid()
        for i in range(PLC_count):
            PLC_square = tk.Frame(PLC_frame, width=square_size, height=square_size, bg='blue')
            PLC_square.grid(row=i//(int(config.get('Settings', 'distributionX'))), column=i%(int(config.get('Settings', 'distributionY'))), padx=5, pady=5)
            PLC_square.bind('<Button-1>', lambda event : on_square_click(i))
            PLC_Squares.append(PLC_square)  

def on_square_click(plc_num):
    PLC_frame.grid_forget()
    Bit_frame.grid()
    create_bit_squares(plc_num)

def on_back_button_click():
    Bit_Squares.clear()
    Bit_frame.grid_forget()
    create_PLC_squares()


config = configparser.ConfigParser()
config.read('Snap-7-Projects\SCADA Programs\SCADA 200\config.ini')
square_size = int(config.get('Settings', 'square_size'))
PLC_count = int(config.get('Settings', 'PLC_count'))
bytes_in_read = int(config.get('Settings', 'bytes_in_read'))
bytes_out_read = int(config.get('Settings', 'bytes_out_read'))
PLC_count = int(config.get('Settings', 'PLC_count'))
window = tk.Tk()
window.title("Programa de Cuadrados")
PLC_frame = tk.Frame(window, bg='lightblue')
Bit_frame = tk.Frame(window, bg='lightgreen')
back_button = tk.Button(window, text='Atrás', command=on_back_button_click)
PLC_Squares = []
Bit_Squares = []

create_PLC_squares()
    
window.mainloop()