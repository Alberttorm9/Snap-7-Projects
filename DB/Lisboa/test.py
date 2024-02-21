import tkinter as tk
import sys
from tkinter import simpledialog

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="¿Estás seguro de que quieres salir?").grid(row=0)

    def buttonbox(self):
        box = tk.Frame(self)

        tk.Button(box, text="Sí, quiero salir", width=10, command=self.yes, default="active").pack(side="left", padx=5, pady=5)
        tk.Button(box, text="No, quiero quedarme", width=10, command=self.no).pack(side="left", padx=5, pady=5)

        self.bind("<Return>", self.yes)
        self.bind("<Escape>", self.no)

        box.pack()

    def yes(self, event=None):
        self.ok()
        sys.exit()

    def no(self, event=None):
        self.cancel()

root = tk.Tk()

def close_window():
    CustomDialog(root)

root.protocol("WM_DELETE_WINDOW", close_window)
root.mainloop()
