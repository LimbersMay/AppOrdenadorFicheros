from tkinter import *
from configuracion import Configuracion

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

        # Objeto al que observaremos para obtener los cambios de la configuración
        self.configuracion = Configuracion('json/configuracion.json')

        # Partes del programa
        self.titulo = Titulo(self)
        self.campos_rutas = BotonRuta(self)
        self.tabla = Tabla(self)
        self.botones = Boton(self)

        # Enviamos el objeto al que observaremos para obtener los cambios de la configuración
        self.botones.agregar_observado(self.configuracion)
        self.campos_rutas.agregar_observado(self.configuracion)

        # Le indicamos al objeto observado quiénes son sus observadores
        self.configuracion.agregar_observador(self.botones)
        self.configuracion.agregar_observador(self.campos_rutas)

        # Notificamos a todos los observadores cúales son las configuraciones actuales
        self.configuracion.notificar()

        # Posicionamiento
        self.titulo.grid(row=1, column=1)
        self.campos_rutas.grid(row=2, column=1)
        self.tabla.grid(row=3, column=1)
        self.botones.grid(row=4, column=1)
        