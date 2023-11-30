import tkinter as tk
import configparser
import PLC_Updater
import time

def create_bit_squares(plc_num):
    global bit_squares_created
    if bit_squares_created == False:
        lista_variables = PLC_Updater.actualizador(plc_num)
        print("c")
        print(lista_variables)
        time.sleep(5)
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
        bit_squares_created = True
    else:
        lista_variables = PLC_Updater.actualizador(plc_num)
        print("b")
        print(lista_variables)
        time.sleep(5)
        for j in range(bytes_in_read):
            for k in range(7):
                if not (lista_variables[0][j][k]):
                    Bit_Squares[(int(j*7))].config(bg='red')
                else:
                    Bit_Squares[(int(j*7))].config(bg='green')

        for j in range(bytes_out_read):
            for k in range(7):
                if not (lista_variables[1][j][k]):
                    Bit_Squares[(int(j+((bytes_in_read+j)*7)))].config(bg='blue')
                else:
                    Bit_Squares[(int(j+((bytes_in_read+j)*7)))].config(bg='yellow')

    print("a")
    window.after(3000, lambda: create_bit_squares(plc_num)) 

def create_PLC_squares():
        PLC_frame.grid()
        for i in range(PLC_count):
            PLC_square = tk.Frame(PLC_frame, width=square_size, height=square_size, bg='blue')
            PLC_square.grid(row=i//(int(config.get('Settings', 'distributionX'))), column=i%(int(config.get('Settings', 'distributionY'))), padx=5, pady=5)
            print(f'El valor es {i}')
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