import tkinter as tk
import configparser
import PLC_Updater
import time

def create_bit_squares(plc_num):
    global bit_squares_created, after_id
    if bit_squares_created == False:
        lista_variables = PLC_Updater.actualizador(plc_num)
        for j in range(bytes_in_read):
            for k in range(8):
                if not (lista_variables[0][j][k]):
                    color = "red"
                else:
                    color = "green"
                Bit_square = tk.Canvas(Bit_frame, width=50, height=50, bg=color)
                Bit_square.create_text(25, 25, text=f'Bit I{j}.{k}', fill='black')
                Bit_square.grid(row=j, column=k, padx=5, pady=5)
                Bit_Squares.append(Bit_square)
        for j in range(bytes_out_read):
            for k in range(8):
                if not (lista_variables[1][j][k]):
                    color = "white"
                else:
                    color = "lightblue"
                Bit_square = tk.Canvas(Bit_frame, width=50, height=50, bg=color)
                Bit_square.create_text(25, 25, text=f'Bit Q{j}.{k}', fill='black')
                Bit_square.grid(row=(j + int(config.get('Settings', 'bytes_in_read'))), column=k, padx=5, pady=5)  
                Bit_Squares.append(Bit_square)
        bit_squares_created = True
        bit_squares_created = True
    else:
        lista_variables = PLC_Updater.actualizador(plc_num)
        for j in range(bytes_in_read):
            for k in range(8):       
                if not (lista_variables[0][j][k]):
                    Bit_Squares[(k+(j*8))].config(bg='red')
                else:
                    Bit_Squares[(k+(j*8))].config(bg='green')

        for j in range(bytes_out_read):
            for k in range(8):
                if not (lista_variables[1][j][k]):
                    Bit_Squares[(k+((j*8)+(bytes_in_read*8)))].config(bg='white')
                else:
                    Bit_Squares[(k+((j*8)+(bytes_in_read*8)))].config(bg='lightblue')
   
    after_id = window.after(1000, lambda: create_bit_squares(plc_num))
    back_button = tk.Button(Bit_frame, text='Atrás', command= lambda:on_back_button_click(after_id))
    back_button.grid(row=0, column=8, columnspan=2, pady=10)

def create_PLC_squares():
    PLC_frame.grid()
    for i in range(PLC_count):
        PLC_square = tk.Canvas(PLC_frame, width=square_size, height=square_size, bg='blue')
        PLC_square.create_text(square_size // 2, square_size // 2, text=f'PLC {i+1}', fill='white')
        PLC_square.bind('<Button-1>', lambda event, plc_num=i: on_square_click(plc_num))
        PLC_square.grid(row=i//(int(config.get('Settings', 'distributionX'))), column=i%(int(config.get('Settings', 'distributionY'))), padx=5, pady=5)
        PLC_Squares.append(PLC_square)  

def on_square_click(plc_num):
    PLC_frame.grid_forget()
    Bit_frame.grid()
    create_bit_squares(plc_num)

def on_back_button_click(after_id):
    global bit_squares_created
    window.after_cancel(after_id)
    Bit_Squares.clear()
    bit_squares_created = False
    Bit_frame.grid_forget()
    create_PLC_squares()


config = configparser.ConfigParser()
config.read(r'SCADA Programs\SCADA 200\config.ini')
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
bit_squares_created = False
after_id = None
create_PLC_squares()
   
window.mainloop()