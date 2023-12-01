import tkinter as tk
import configparser
import PLC_Updater
import time

def create_bit_squares(plc_num):
    global bit_squares_created
    if bit_squares_created == False:
        lista_variables = PLC_Updater.actualizador(plc_num)
        time.sleep(5)
        for j in range(bytes_in_read):
            for k in range(7):
                if not (lista_variables[0][j][k]):
                    color = "red"
                else:
                    color = "green"
                Bit_square = tk.Frame(Bit_frame, width=50, height=50, bg=color)
                Bit_square.grid(row=j, column=k, padx=5, pady=5)
                Bit_Squares.append(Bit_square)

        for j in range(bytes_out_read):
            for k in range(7):
                if not (lista_variables[1][j][k]):
                    color = "blue"
                else:
                    color = "yellow"
                Bit_square = tk.Frame(Bit_frame, width=50, height=50, bg=color)
                Bit_square.grid(row=(j + int(config.get('Settings', 'bytes_in_read'))), column=k, padx=5, pady=5)  
                Bit_Squares.append(Bit_square)
        bit_squares_created = True
    else:
        lista_variables = PLC_Updater.actualizador(plc_num)
        time.sleep(5)
        a = 0 ####
        for j in range(bytes_in_read):
            for k in range(7):
                if not (lista_variables[0][j][k]):
                    a += 1 ####
                    print(a)
                    Bit_Squares[(int(k+(j*bytes_in_read)))].config(bg='red')
                else:
                    a += 1 ####
                    print(f'{a}' + "w")
                    Bit_Squares[(int(k+(j*bytes_in_read)))].config(bg='green')

        for j in range(bytes_out_read):
            for k in range(7):
                if not (lista_variables[1][j][k]):
                    Bit_Squares[(int(j+((bytes_in_read+j)*7)))].config(bg='blue')
                else:
                    Bit_Squares[(int(j+((bytes_in_read+j)*7)))].config(bg='yellow') 
    after_id = window.after(1000, lambda: create_bit_squares(plc_num))
    back_button = tk.Button(Bit_frame, text='Atrás', command=on_back_button_click(after_id))
    back_button.grid(row=0, column=8, columnspan=2, pady=10)#Problema con el boton
def create_PLC_squares():
        PLC_frame.grid()
        for i in range(PLC_count):
            PLC_square = tk.Frame(PLC_frame, width=square_size, height=square_size, bg='blue')
            PLC_square.bind('<Button-1>', lambda event, plc_num=i: on_square_click(plc_num))
            PLC_square.grid(row=i//(int(config.get('Settings', 'distributionX'))), column=i%(int(config.get('Settings', 'distributionY'))), padx=5, pady=5)
            print(f'El valor 1 es {i}')
            PLC_Squares.append(PLC_square)  

def on_square_click(plc_num):
    print(f'El valor 2 es {plc_num}')
    PLC_frame.grid_forget()
    Bit_frame.grid()
    create_bit_squares(plc_num)

def on_back_button_click(after_id):
    window.after_cancel(after_id)
    Bit_Squares.clear()
    Bit_frame.grid_forget()
    create_PLC_squares()


config = configparser.ConfigParser()
config.read(r'Snap-7-Projects\SCADA Programs\SCADA 200\config.ini')
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
create_PLC_squares()
    
window.mainloop()