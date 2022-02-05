from tkinter import *
from ventana_config.titulo import Titulo
from ventana_config.opcion import Opcion
from ventana_config.boton_guardar import BotonGuardar

class VentanaConfiguracion(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Configuraciones del master
        master.title("Configuraciones")
        master.geometry("370x150")
        master.config(bg="#2c2b33")

        # Configuraciones del frame
        self.config(bg="#2c2b33")

        # Partes del programa
        self.titulo = Titulo(self)
        self.opcion = Opcion(self)
        self.boton_guardar = BotonGuardar(self)

        # Posicionamiento de los objetos
        self.titulo.grid(row=1, column=1)
        self.opcion.grid(row=2, column=1)
        self.boton_guardar.grid(row=3, column=1)