from tkinter import *

from botones_inferiores import Boton
from botones_rutas import BotonRuta
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
        campos_rutas = BotonRuta(self)
        tabla = Tabla(self)
        botones = Boton(self)

        # Posicionamiento
        titulo.grid(row=1, column=1)
        campos_rutas.grid(row=2, column=1)
        tabla.grid(row=3, column=1)
        botones.grid(row=4, column=1)
        