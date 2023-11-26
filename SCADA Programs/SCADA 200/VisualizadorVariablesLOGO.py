
import tkinter as tk
import configparser
import PLC_Updater

class App:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config_Prueba.ini')
        self.square_size = int(self.config.get('Settings', 'square_size'))
        self.PLC_count = int(self.config.get('Settings', 'PLC_count'))
        self.window = tk.Tk()
        self.window.title("Programa de Cuadrados")
        self.create_squares()
    
    def create_squares(self):
        self.squares = []
        for i in range(self.PLC_count):
            square = tk.Frame(self.window, width=self.square_size, height=self.square_size, bg='blue')
            square.grid(row=i//(int(self.config.get('Settings', 'distributionX'))), column=i%(int(self.config.get('Settings', 'distributionY'))), padx=5, pady=5)
            square.bind('<Button-1>', self.on_square_click)
            self.squares.append(square)
    
    def on_square_click(self, event):
        for square in self.squares:
            square.grid_forget()
        self.create_large_squares()
    
    def create_large_squares(self):
        self.large_squares = []
        bytes_a_leer = int(self.config.get('Settings', 'bytes_in_read'))
        byte_in_leido = 0
        byte_out_leido = 0
        for j in range(bytes_a_leer):
            byte_in_leido = byte_in_leido + 1
            for i in range(7):
                estado_bit_in = PLC_Updater.lista_in
                if not (estado_bit_in[i*byte_in_leido]):
                    color = "red"
                else:
                    color = "green"
                square = tk.Frame(self.window, width=50, height=50, bg=color)
                square.grid(row=j, column=i, padx=5, pady=5)
                self.large_squares.append(square)
        for j in range(int(self.config.get('Settings', 'bytes_out_read'))):
            byte_out_leido = byte_out_leido + 1
            for i in range(7):
                estado_bit_out = PLC_Updater.lista_out
                if not (estado_bit_out[i*byte_out_leido]):
                    color = "blue"
                else:
                    color = "yellow"
                square = tk.Frame(self.window, width=50, height=50, bg=color)
                square.grid(row=(j + int(self.config.get('Settings', 'bytes_in_read'))), column=i, padx=5, pady=5)
                self.large_squares.append(square)    
        back_button = tk.Button(self.window, text='Atrás', command=self.on_back_button_click)
        back_button.grid(row=0, column=8, columnspan=2, pady=10)
        self.back_button = back_button
    
    def on_back_button_click(self):
        for square in self.large_squares:
            square.grid_forget()
        self.back_button.grid_forget()
        self.create_squares()

app = App()
app.window.mainloop()