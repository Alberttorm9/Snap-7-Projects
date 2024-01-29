import tkinter as tk
from tkinter import PhotoImage, ttk
from PIL import Image, ImageTk
import customtkinter as ctk
import os
import sys
from datetime import datetime, date, timedelta
from openpyxl.styles import Font


#####################################################################################################################################################

# Interfaz de usuario
root = tk.Tk()
root.title("Exportar Información")
root.config(bg='#505050')

#####################################################################################################################################################

Plano = ImageTk.PhotoImage(file=os.path.abspath("PLANO.png"))
Boton = ImageTk.PhotoImage(file=os.path.abspath("Boton.png"))

#####################################################################################################################################################

PlanoLabel = tk.Label(root, image=Plano, borderwidth=0)
PlanoLabel.place(x=0, y=0)


Boton_Peticion_Salida = tk.Label(root, image=Boton, highlightthickness=0, borderwidth=0)
Boton_Peticion_Salida.place(x=0, y=0)


root.mainloop()