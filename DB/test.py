import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('800x800')
root.title('Exportaciones')

window_width = 800
window_height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')

style = ttk.Style()
style.configure('Custom.TButton', font=('Helvetica', 12), padding=10)

frame_exportaciones = ttk.Frame(root)
frame_exportaciones.place(relx=0.5, rely=0.5, anchor='center')

open_frame_reportes = ttk.Button(frame_exportaciones, text="Exportar Reportes", style='Custom.TButton')
open_frame_reportes.grid(row=0, column=0, padx=10, pady=10)

open_frame_exit = ttk.Button(frame_exportaciones, text="Exportar Salidas Del Sistema", style='Custom.TButton')
open_frame_exit.grid(row=0, column=1, padx=10, pady=10)

open_frame_habs = ttk.Button(frame_exportaciones, text="Exportar Limpieza Habitaciones", style='Custom.TButton')
open_frame_habs.grid(row=0, column=2, padx=10, pady=10)


root.mainloop()