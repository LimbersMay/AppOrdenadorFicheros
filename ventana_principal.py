from tkinter import *

from principal.botones_inferiores import Boton
from principal.botones_rutas import BotonRuta
from principal.tabla import Tabla
from principal.titulo import Titulo

class Ventana(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Configuración básica
        master.title("Organizador de archivos")
        master.geometry("500x350")
        master.config(bg="#2c2b33")

        self.config(bg="#2c2b33")

        # Partes del programa
        self.titulo = Titulo(self)
        self.campos_rutas = BotonRuta(self)
        self.tabla = Tabla(self)
        self.botones = Boton(self)

        # Posicionamiento
        self.titulo.grid(row=1, column=1)
        self.campos_rutas.grid(row=2, column=1)
        self.tabla.grid(row=3, column=1)
        self.botones.grid(row=4, column=1)
        