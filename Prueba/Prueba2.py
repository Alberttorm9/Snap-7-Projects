import tkinter as tk

class ImageSlider(tk.Frame):
    def __init__(self, master, images):
        tk.Frame.__init__(self, master)
        self.images = images
        self.current_image = 0

        self.image_label = tk.Label(self)
        self.image_label.pack()

        self.prev_button = tk.Button(self, text="Anterior", command=self.show_previous_image)
        self.prev_button.pack(side="left")
        self.next_button = tk.Button(self, text="Siguiente", command=self.show_next_image)
        self.next_button.pack(side="right")

    def show_image(self):
        image_path = self.images[self.current_image]
        image = tk.PhotoImage(file=image_path)
        self.image_label.config(image=image)
        self.image_label.image = image  # Evita que la imagen sea eliminada por el recolector de basura

    def show_previous_image(self):
        self.current_image = (self.current_image - 1) % len(self.images)
        self.show_image()

    def show_next_image(self):
        self.current_image = (self.current_image + 1) % len(self.images)
        self.show_image()

# Ejemplo de uso
root = tk.Tk()
images = ["Scada\imagenes\imagen1.png", "Scada\imagenes\imagen2.png", "Scada\imagenes\imagen3.png"]  # Lista de rutas de las imágenes
slider = ImageSlider(root, images)
slider.pack()

root.mainloop()