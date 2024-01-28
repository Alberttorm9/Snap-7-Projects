import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        self.entrada = tk.Entry(ventana, width=20, font=("Arial", 16))
        self.entrada.grid(row=0, column=0, columnspan=4)

        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        fila = 1
        columna = 0
        for boton_texto in botones:
            if boton_texto == '=':
                boton = tk.Button(ventana, text=boton_texto, width=10, command=self.calcular)
            elif boton_texto == 'C':
                boton = tk.Button(ventana, text=boton_texto, width=10, command=self.limpiar)
            else:
                boton = tk.Button(ventana, text=boton_texto, width=5, command=lambda texto=boton_texto: self.anadir_texto(texto))
            boton.grid(row=fila, column=columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

    def anadir_texto(self, texto):
        self.entrada.insert(tk.END, texto)

    def limpiar(self):
        self.entrada.delete(0, tk.END)

    def calcular(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

# Crear ventana
ventana = tk.Tk()
mi_calculadora = Calculadora(ventana)

# Ejecutar ventana
ventana.mainloop()