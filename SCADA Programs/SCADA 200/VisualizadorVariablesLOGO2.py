import tkinter as tk
from PIL import ImageTk, Image
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

def on_PLC_button_click(i):
    print('PLC {} button clicked'.format(i+1))

def create_PLC_squares():
    global PLC_Squares, Bit_Squares, bit_squares_created, after_id, after_id_2

    # Create PLC squares
    PLC_Squares = [tk.Button(PLC_frame, text='PLC {}'.format(i+1), width=10, height=2, command=lambda i=i: on_PLC_button_click(i)) for i in range(PLC_count)]
    for i, sq in enumerate(PLC_Squares):
        sq.grid(row=i//5, column=i%5)

    # Create Bit squares
    Bit_Squares = [tk.Label(Bit_frame, text='Bit {}'.format(i+1), width=10, height=2, bg='white') for i in range(bytes_in_read*8)]
    for i, sq in enumerate(Bit_Squares):
        sq.grid(row=i//8, column=i%8)

    # Create back button
    back_button = tk.Button(window, text='Atrás', command=on_back_button_click)
    back_button.pack()

    # Initialize the text of the button
    button_text = tk.StringVar()
    button_text.set('Update')

    # Create the update button
    update_button = tk.Button(window, textvariable=button_text, width=10, height=2, command=lambda: update_button_text(button_text))
    update_button.pack()

    # Start updating the button text
    after_id = window.after(1000, update_button_text, button_text)
   
def update_button_text(button_text):
    new_text = 'Update ({})'.format(bytes_out_read)
    button_text.set(new_text)

def on_square_click(plc_num):
    window.after_cancel(after_id_2) 
    PLC_frame.grid_forget()
    Bit_frame.grid()
    create_bit_squares(plc_num)

def on_back_button_click(after_id):
    global bit_squares_created, Bit_frame
    if after_id is not None:
        window.after_cancel(after_id)
    Bit_Squares.clear()
    bit_squares_created = False
    Bit_frame.grid_forget()
    create_PLC_squares()
    Bit_frame.destroy()
    Bit_frame = tk.Frame(window, bg='lightgreen')

def limit_frequency(func):
    last_time_called = [0.0]
    def wrapper(*args, **kwargs):
        elapsed = time.time() - last_time_called[0]
        if elapsed < 1.0:
            return
        last_time_called[0] = time.time()
        return func(*args, **kwargs)
    return wrapper

config = configparser.ConfigParser()
config.read('config.ini')
square_size = int(config.get('Settings', 'square_size'))
PLC_count = int(config.get('Settings', 'PLC_count'))
bytes_in_read = int(config.get('Settings', 'bytes_in_read'))
bytes_out_read = int(config.get('Settings', 'bytes_out_read'))
PLC_count = int(config.get('Settings', 'PLC_count'))
window = tk.Tk()
window.title("SCADA")
PLC_frame = tk.Frame(window, bg='lightblue')
Bit_frame = tk.Frame(window, bg='lightgreen')
back_button = tk.Button(window, text='Atrás', command=on_back_button_click)
PLC_Squares = []
Bit_Squares = []
bit_squares_created = False
after_id = None
after_id_2 = None


#Image src
imagen = Image.open("Logo-icono.png")
imagen = imagen.resize((90, 90))
image_PLC = ImageTk.PhotoImage(imagen)

update_button_text = limit_frequency(update_button_text)

create_PLC_squares()
   
window.mainloop()