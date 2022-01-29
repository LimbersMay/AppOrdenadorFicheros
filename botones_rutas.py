from tkinter import *

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
        ruta_origen_label = Label(self, text="Ruta origen:")
        ruta_destino_label = Label(self, text="Ruta destino:")