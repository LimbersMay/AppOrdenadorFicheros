from tkinter import *

from botones_inferiores import Boton
from tabla import Tabla
from titulo import Titulo

class Ventana(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Configuración básica
        master.title("Organizador de archivos")
        master.geometry("500x500")
        master.config(bg="#2c2b33")

        # Partes del programa
        titulo = Titulo(self)
        tabla = Tabla(self)
        botones = Boton(self)

        titulo.grid(row=1, column=1)
        tabla.grid(row=2, column=2)
        botones.grid(row=3, column=3)
        