import tkinter as tk
import configparser
import PLC_Updater
import Connection_Ok as ts
import time

def create_bit_squares(plc_num):
    global bit_squares_created, after_id
    if bit_squares_created == False:
        lista_variables = PLC_Updater.actualizador(plc_num)
        if lista_variables != 0:
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
        else:
            Bit_square = tk.Canvas(Bit_frame, width=120, height=30, bg="red")
            Bit_square.create_text(60, 15, text="PLC Desconectado", fill='black', anchor='center')
            Bit_square.grid(row=0, column=0, padx=5, pady=5)
            bit_squares_created = False
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
    if bit_squares_created:
        after_id = window.after(1000, lambda: create_bit_squares(plc_num))
    back_button = tk.Button(Bit_frame, text='Atrás', command= lambda:on_back_button_click(after_id))
    back_button.grid(row=0, column=8, columnspan=2, pady=10)

def create_PLC_squares():
    global after_id_2
    PLC_frame.grid()
    for i in range(PLC_count):
        bg_selector = ts.try_to_connect(f'192.168.30.{i+101}',0,1)
        if bg_selector==True:
            bg_selector = "Green"
        else:
            bg_selector = "Red"
        PLC_square = tk.Canvas(PLC_frame, width=square_size, height=square_size, bg=bg_selector)
        PLC_square.create_text(square_size // 2, square_size // 2, text=f'PLC {i+1}', fill='white')
        PLC_square.bind('<Button-1>', lambda event, plc_num=i: on_square_click(plc_num))
        PLC_square.grid(row=i//(int(config.get('Settings', 'distributionX'))), column=i%(int(config.get('Settings', 'distributionY'))), padx=5, pady=5)
        PLC_Squares.append(PLC_square) 
        if i==PLC_count-1:
            after_id_2 = window.after(2500, create_PLC_squares)     

def on_square_click(plc_num):
    window.after_cancel(after_id_2) 
    PLC_frame.grid_forget()
    Bit_frame.grid()
    create_bit_squares(plc_num)

def on_back_button_click(after_id):
    global bit_squares_created, Bit_frame
    window.after_cancel(after_id)
    Bit_Squares.clear()
    bit_squares_created = False
    Bit_frame.grid_forget()
    create_PLC_squares()
    Bit_frame.destroy()
    Bit_frame = tk.Frame(window, bg='lightgreen')


config = configparser.ConfigParser()
config.read(r'C:\Users\alber\Documents\Snap-7-Projects\SCADA Programs\SCADA 200\config.ini')
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
after_id_2 = None
create_PLC_squares()
   
window.mainloop()