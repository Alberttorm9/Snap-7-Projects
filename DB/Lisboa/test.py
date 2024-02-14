import tkinter as tk
import configparser

def adjust_size(width, height):
    new_font_size = min(width // 20, height // 20)
    OpenFrameReportes.config(font=("Arial", new_font_size))

# Leer la configuración desde el archivo .ini
config = configparser.ConfigParser()
config.read('config2.ini')
width = config.getint('GUI', 'width')
height = config.getint('GUI', 'height')

root = tk.Tk()
root.geometry(f"{width}x{height}")

# Suponiendo que 'OpenFrameReportes' es un botón de tu interfaz
OpenFrameReportes = tk.Button(root, text="Exportar Reportes", font=("Arial", 40))
OpenFrameReportes.grid(row=1, column=0, padx=10, pady=10)

# Llamamos a adjust_size una vez al inicio para ajustar el tamaño
adjust_size(width, height)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()