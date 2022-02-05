from tkinter import *
from ventana_config.titulo import Titulo

class VentanaConfiguracion(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Configuraciones del master
        master.title("Configuraciones")
        master.geometry("370x350")
        master.config(bg="#2c2b33")

        # Configuraciones del frame
        self.config(bg="#2c2b33")

        # Partes del programa
        self.titulo = Titulo(self)

        # Posicionamiento de los objetos
        self.titulo.grid(row=1, column=1)