import tkinter as tk

# Función para cerrar la ventana emergente después de 2 segundos
def cerrar_ventana():
    ventana_emergente.destroy()

# Crear la ventana principal
root = tk.Tk()

# Configurar la geometría y otras propiedades
ScreenGeometry = "200x200"  # Aquí tu ScreenGeometry
root.geometry(ScreenGeometry)
root.overrideredirect(True)
root.attributes("-topmost", True)

# Crear la ventana emergente
ventana_emergente = tk.Toplevel(root)
ventana_emergente.title("Ventana Emergente")
ventana_emergente.geometry("150x100+200+200")

# Llamar a la función para cerrar la ventana emergente después de 2 segundos
root.after(2000, cerrar_ventana)

# Iniciar el bucle principal
root.mainloop()