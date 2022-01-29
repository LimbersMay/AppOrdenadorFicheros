from tkinter import *

from matplotlib.pyplot import grid

class BotonRuta(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Configuraciones
        self.config(
            bg="white",
            width=500,
            height=50
        )

        self.grid_propagate(False)

        # Partes del programa
        # Textos de las rutas
        self.ruta_origen_label = Label(self, text="Ruta origen:")
        self.ruta_destino_label = Label(self, text="Ruta destino:")

        # Campos para introducir las rutas
        self.ruta_origen_entry = Entry(self)
        self.ruta_destino_entry = Entry(self)

        # Botones para seleccionar las rutas
        self.ruta_origen_button = Button(self, text="Seleccionar ruta")
        self.ruta_destino_button = Button(self, text="Seleccionar ruta")

        # Posicionamiento
    